import json
from pathlib import Path

import pytest

from week08.lab08 import FavoritesManager


@pytest.fixture
def fav_file(tmp_path: Path) -> Path:
    return tmp_path / "favorites.json"


def test_add_favorite(fav_file: Path):
    m = FavoritesManager(fav_file)
    assert m.add("home", "Cincinnati, OH") is True
    assert m.get_location("home") == "Cincinnati, OH"


def test_add_duplicate_case_insensitive(fav_file: Path):
    m = FavoritesManager(fav_file)
    assert m.add("Home", "Cincinnati, OH") is True
    assert m.add("HOME", "Different") is False


def test_remove_favorite(fav_file: Path):
    m = FavoritesManager(fav_file)
    m.add("work", "Columbus, OH")
    assert m.remove("work") is True
    assert m.get_location("work") is None


def test_remove_missing(fav_file: Path):
    m = FavoritesManager(fav_file)
    assert m.remove("missing") is False


def test_list_all(fav_file: Path):
    m = FavoritesManager(fav_file)
    m.add("a", "A City")
    m.add("b", "B City")
    all_favs = m.list_all()
    assert all_favs["a"] == "A City"
    assert all_favs["b"] == "B City"


def test_get_location_case_insensitive(fav_file: Path):
    m = FavoritesManager(fav_file)
    m.add("Home", "Cincinnati, OH")
    assert m.get_location("home") == "Cincinnati, OH"
    assert m.get_location("HOME") == "Cincinnati, OH"


def test_persistence_across_instances(fav_file: Path):
    m1 = FavoritesManager(fav_file)
    assert m1.add("home", "Cincinnati, OH") is True

    m2 = FavoritesManager(fav_file)
    assert m2.get_location("home") == "Cincinnati, OH"


def test_loading_nonexistent_file(tmp_path: Path):
    path = tmp_path / "does_not_exist.json"
    m = FavoritesManager(path)
    assert m.list_all() == {}


def test_loading_corrupted_json(fav_file: Path):
    fav_file.write_text("{not valid json", encoding="utf-8")
    m = FavoritesManager(fav_file)
    assert m.list_all() == {}


def test_loading_non_dict_json(fav_file: Path):
    fav_file.write_text(json.dumps(["a", "b"]), encoding="utf-8")
    m = FavoritesManager(fav_file)
    assert m.list_all() == {}
