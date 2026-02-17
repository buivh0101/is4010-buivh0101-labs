"""
Week 08 Lab: Weather CLI Application

Commands:
  python week08/lab08.py current <location_or_favorite>
  python week08/lab08.py forecast <location_or_favorite> --days 1-3
  python week08/lab08.py favorites add <name> <location>
  python week08/lab08.py favorites list
  python week08/lab08.py favorites remove <name>

API key:
  Set WEATHER_API_KEY as an environment variable.
  PowerShell:
    $env:WEATHER_API_KEY="your_key"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict

import requests


# -----------------------------
# Favorites Manager
# -----------------------------
class FavoritesManager:
    """
    Manage favorite locations stored in a JSON file.

    Favorites are case-insensitive by name.
    Stored format on disk: { "home": "Cincinnati, OH", "work": "Columbus, OH" }
    """

    def __init__(self, file_path: Path):
        self.file_path = Path(file_path)
        self._favorites: Dict[str, str] = {}
        self._load()

    @staticmethod
    def _norm(name: str) -> str:
        return name.strip().casefold()

    def _load(self) -> None:
        if not self.file_path.exists():
            self._favorites = {}
            return

        try:
            text = self.file_path.read_text(encoding="utf-8")
            data = json.loads(text)
            if not isinstance(data, dict):
                self._favorites = {}
                return

            cleaned: Dict[str, str] = {}
            for k, v in data.items():
                if isinstance(k, str) and isinstance(v, str):
                    cleaned[self._norm(k)] = v.strip()
            self._favorites = cleaned

        except (OSError, json.JSONDecodeError):
            # Corrupted or unreadable file. Treat as empty.
            self._favorites = {}

    def _save(self) -> None:
        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            # Save with original normalized keys
            self.file_path.write_text(
                json.dumps(self._favorites, indent=2, sort_keys=True),
                encoding="utf-8",
            )
        except OSError:
            # Do not crash CLI on save failure
            pass

    def add(self, name: str, location: str) -> bool:
        key = self._norm(name)
        if key in self._favorites:
            return False
        self._favorites[key] = location.strip()
        self._save()
        return True

    def remove(self, name: str) -> bool:
        key = self._norm(name)
        if key not in self._favorites:
            return False
        del self._favorites[key]
        self._save()
        return True

    def list_all(self) -> Dict[str, str]:
        # Return a copy
        return dict(self._favorites)

    def get_location(self, name: str) -> Optional[str]:
        return self._favorites.get(self._norm(name))


# -----------------------------
# Weather API Client
# -----------------------------
@dataclass(frozen=True)
class WeatherAPI:
    api_key: str
    base_url: str = "http://api.weatherapi.com/v1"

    def get_current_weather(self, location: str) -> Optional[dict]:
        url = f"{self.base_url}/current.json"
        params = {"key": self.api_key, "q": location}
        try:
            resp = requests.get(url, params=params, timeout=10)
            if resp.status_code != 200:
                return None
            return resp.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

    def get_forecast(self, location: str, days: int = 3) -> Optional[dict]:
        url = f"{self.base_url}/forecast.json"
        params = {"key": self.api_key, "q": location, "days": days}
        try:
            resp = requests.get(url, params=params, timeout=10)
            if resp.status_code != 200:
                return None
            return resp.json()
        except (requests.exceptions.RequestException, ValueError):
            return None


# -----------------------------
# Formatting Helpers
# -----------------------------
def _safe_get(d: dict, *keys, default="N/A"):
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def format_current_weather(data: dict) -> str:
    name = _safe_get(data, "location", "name")
    region = _safe_get(data, "location", "region")
    country = _safe_get(data, "location", "country")

    condition = _safe_get(data, "current", "condition", "text")
    temp_f = _safe_get(data, "current", "temp_f")
    temp_c = _safe_get(data, "current", "temp_c")
    feels_f = _safe_get(data, "current", "feelslike_f")
    feels_c = _safe_get(data, "current", "feelslike_c")
    humidity = _safe_get(data, "current", "humidity")
    wind_mph = _safe_get(data, "current", "wind_mph")
    wind_dir = _safe_get(data, "current", "wind_dir")
    updated = _safe_get(data, "current", "last_updated")

    title = f"Current Weather for {name}"
    if region != "N/A" and region:
        title += f", {region}"
    if country != "N/A" and country:
        title += f", {country}"

    line = "=" * 50
    return "\n".join(
        [
            line,
            title,
            line,
            f"Condition: {condition}",
            f"Temperature: {temp_f}°F ({temp_c}°C)",
            f"Feels Like: {feels_f}°F ({feels_c}°C)",
            f"Humidity: {humidity}%",
            f"Wind: {wind_mph} mph {wind_dir}",
            f"Last Updated: {updated}",
            line,
        ]
    )


def format_forecast(data: dict) -> str:
    name = _safe_get(data, "location", "name")
    region = _safe_get(data, "location", "region")
    country = _safe_get(data, "location", "country")

    title = f"Forecast for {name}"
    if region != "N/A" and region:
        title += f", {region}"
    if country != "N/A" and country:
        title += f", {country}"

    line = "=" * 50

    days = _safe_get(data, "forecast", "forecastday", default=[])
    if not isinstance(days, list) or len(days) == 0:
        return "\n".join([line, title, line, "No forecast data available.", line])

    rows = []
    for day in days:
        date = _safe_get(day, "date")
        cond = _safe_get(day, "day", "condition", "text")
        max_f = _safe_get(day, "day", "maxtemp_f")
        min_f = _safe_get(day, "day", "mintemp_f")
        max_c = _safe_get(day, "day", "maxtemp_c")
        min_c = _safe_get(day, "day", "mintemp_c")
        rows.append(f"{date}: {cond} | High {max_f}°F/{max_c}°C | Low {min_f}°F/{min_c}°C")

    return "\n".join([line, title, line, *rows, line])


# -----------------------------
# CLI Handlers
# -----------------------------
def _get_api_key_or_exit() -> str:
    key = os.getenv("WEATHER_API_KEY", "").strip()
    if not key:
        print("Missing API key. Set WEATHER_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)
    return key


def _favorites_path() -> Path:
    # Store favorites.json inside week08 folder
    return Path(__file__).resolve().parent / "favorites.json"


def _resolve_location(raw: str, favs: FavoritesManager) -> str:
    found = favs.get_location(raw)
    return found if found else raw


def handle_current(args: argparse.Namespace) -> None:
    favs = FavoritesManager(_favorites_path())
    location = _resolve_location(args.location, favs)

    api = WeatherAPI(_get_api_key_or_exit())
    data = api.get_current_weather(location)
    if data is None:
        print("Failed to fetch current weather. Check location, API key, or network.", file=sys.stderr)
        sys.exit(2)

    print(format_current_weather(data))


def handle_forecast(args: argparse.Namespace) -> None:
    favs = FavoritesManager(_favorites_path())
    location = _resolve_location(args.location, favs)

    api = WeatherAPI(_get_api_key_or_exit())
    data = api.get_forecast(location, days=args.days)
    if data is None:
        print("Failed to fetch forecast. Check location, API key, or network.", file=sys.stderr)
        sys.exit(2)

    print(format_forecast(data))


def handle_fav_add(args: argparse.Namespace) -> None:
    favs = FavoritesManager(_favorites_path())
    ok = favs.add(args.name, args.location)
    if not ok:
        print(f"Favorite '{args.name}' already exists.", file=sys.stderr)
        sys.exit(2)
    print(f"Added favorite '{args.name}' -> {args.location}")


def handle_fav_remove(args: argparse.Namespace) -> None:
    favs = FavoritesManager(_favorites_path())
    ok = favs.remove(args.name)
    if not ok:
        print(f"Favorite '{args.name}' not found.", file=sys.stderr)
        sys.exit(2)
    print(f"Removed favorite '{args.name}'")


def handle_fav_list(args: argparse.Namespace) -> None:
    favs = FavoritesManager(_favorites_path())
    all_favs = favs.list_all()
    if not all_favs:
        print("No favorites saved.")
        return

    print("Favorites:")
    for name, loc in sorted(all_favs.items()):
        print(f"  {name}: {loc}")


# -----------------------------
# Argparse setup
# -----------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="lab08.py", description="Weather CLI Application")
    sub = parser.add_subparsers(dest="command", required=True)

    p_current = sub.add_parser("current", help="Get current weather")
    p_current.add_argument("location", help="City name or favorite name")
    p_current.set_defaults(func=handle_current)

    p_forecast = sub.add_parser("forecast", help="Get weather forecast")
    p_forecast.add_argument("location", help="City name or favorite name")
    p_forecast.add_argument("--days", type=int, default=3, choices=[1, 2, 3], help="Forecast days (1-3)")
    p_forecast.set_defaults(func=handle_forecast)

    p_fav = sub.add_parser("favorites", help="Manage favorites")
    fav_sub = p_fav.add_subparsers(dest="fav_cmd", required=True)

    p_add = fav_sub.add_parser("add", help="Add a favorite")
    p_add.add_argument("name", help="Favorite name (example: home)")
    p_add.add_argument("location", help='Location string (example: "Cincinnati, OH")')
    p_add.set_defaults(func=handle_fav_add)

    p_list = fav_sub.add_parser("list", help="List favorites")
    p_list.set_defaults(func=handle_fav_list)

    p_rm = fav_sub.add_parser("remove", help="Remove a favorite")
    p_rm.add_argument("name", help="Favorite name to remove")
    p_rm.set_defaults(func=handle_fav_remove)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
