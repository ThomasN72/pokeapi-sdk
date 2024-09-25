import pytest
from pokeapi_sdk.client import PokeAPIClient
from pokeapi_sdk.errors import PokemonNotFoundError


class TestPokeapiSDK:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.sdk = PokeAPIClient()

    def test_get_pokemon_by_id(self):
        """Test fetching Pokémon by ID"""
        pokemon_data = self.sdk.get_pokemon(1)
        assert pokemon_data is not None, "Pokemon data should not be None"
        assert pokemon_data["name"] == "bulbasaur", "Expected Pokémon is Bulbasaur"

    def test_get_pokemon_by_name(self):
        """Test fetching Pokémon by Name"""
        pokemon_data = self.sdk.get_pokemon("pikachu")
        assert pokemon_data is not None, "Pokemon data should not be None"
        assert pokemon_data["name"] == "pikachu", "Expected Pokémon is Pikachu"

    def test_invalid_pokemon(self):
        """Test fetching an invalid Pokémon (404 error)"""
        with pytest.raises(PokemonNotFoundError):
            self.sdk.get_pokemon("invalid_pokemon_name")

    def test_get_pokemons(self):
        """Test fetching a paginated list of Pokémon"""
        pokemon_list = self.sdk.get_pokemons(limit=10, offset=0)
        assert pokemon_list is not None, "Pokemon list should not be None"
        assert "results" in pokemon_list, "Expected 'results' key in the response"
        assert len(pokemon_list["results"]) == 10, "Expected 10 Pokémon in the results"

    def test_get_pokemons_with_limit_four(self):
        """Test fetching a paginated list of Pokémon"""
        pokemon_list = self.sdk.get_pokemons(limit=4, offset=20)
        assert pokemon_list is not None, "Pokemon list should not be None"
        assert "results" in pokemon_list, "Expected 'results' key in the response"
        assert len(pokemon_list["results"]) == 4, "Expected 4 Pokémon in the results"

    def test_get_next_page(self):
        """Test pagination by fetching the next page of Pokémon"""
        first_page = self.sdk.get_pokemons(limit=10, offset=0)
        second_page = self.sdk.get_pokemons(limit=10, offset=10)

        assert first_page is not None, "First page should not be None"
        assert second_page is not None, "Second page should not be None"
        assert first_page["results"] != second_page["results"], "The two pages should contain different results"
