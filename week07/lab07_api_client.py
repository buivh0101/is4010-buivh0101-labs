import requests


def get_api_data(url):
    """
    Fetches and parses JSON data from a given API url.

    Parameters
    ----------
    url : str
        The URL of the API endpoint.

    Returns
    -------
    dict or None
        A dictionary containing the parsed JSON data, or None if
        the request fails or the response is not valid JSON.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except ValueError:
        # response.json() raises ValueError if JSON is invalid
        print("Error: Failed to decode JSON from response.")
        return None


if __name__ == "__main__":
    pokemon_url = "https://pokeapi.co/api/v2/pokemon/snorlax"
    pokemon_data = get_api_data(pokemon_url)

    if pokemon_data:
        print(f"Successfully fetched data for: {pokemon_data['name'].title()}")
        print(f"Weight: {pokemon_data['weight']} hectograms")
        print("Abilities:")
        for ability in pokemon_data["abilities"]:
            print(f"  - {ability['ability']['name']}")
