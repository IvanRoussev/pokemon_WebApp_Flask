import pytest
from unittest.mock import patch, mock_open

from pokemon import Pokemon
from collection import Collection

# This is the mock data for Tim's pokemon collection
# It has 5 pokemons

POKEMON_DATA = """{
    "name": "Tim's collection",
    "pokemons": [
        {
            "name": "Pikachu",
            "health": 100,
            "type": "electric"
        },
        {
            "name": "Charmander",
            "health": 0,
            "type": "fire"
        },
        {
            "name": "Beartic",
            "health": 50,
            "type": "ice"
        },
        {
            "name": "Charizard",
            "health": 0,
            "type": "flying"
        },
        {
            "name": "Pidgey",
            "health": 90,
            "type": "flying"
        }
    ]
}
"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=POKEMON_DATA)
def my_collection(mock_file):
    """Standard collection using the mock above"""
    return Collection("tim")


@patch("builtins.open", new_callable=mock_open, read_data=POKEMON_DATA)
def test_tim_collection(mock_file):
    """Check open() calls in the constructor"""
    collection = Collection("Tim")

    # Open the file
    assert mock_file.call_count == 1

    # File is "data/<ARGUMENT IN LOWER CASE>.json"
    assert mock_file.call_args[0][0] == "data/tim.json"


def test_collection_not_exist():
    """When the file does not exist, raise an exception (default behaviour - free mark!)"""
    with pytest.raises(FileNotFoundError):
        Collection("fiesfjlsjfldsfjdslfjlids")


def test_tim_collection_pokemons(my_collection):
    """Check the attributes of the collection"""

    assert my_collection.name == "Tim's collection"

    # Check that all pokemons are Pokemon instances
    for pok in my_collection.pokemons:
        assert type(pok) is Pokemon

    # Check that the list of pokemons is ordered by health descending
    for index, pok in enumerate(my_collection.pokemons[:-1]):
        next_pok = my_collection.pokemons[index + 1]
        assert pok.health >= next_pok.health


def test_tim_collection_by_name(my_collection):
    """Check the find_by_name method - returns a list (only one element in this case)"""
    matching = my_collection.find_by_name("pikachu")
    assert type(matching) is list

    pikachu = matching[0]
    assert type(pikachu) is Pokemon
    assert pikachu.name == "Pikachu"
    assert pikachu.health == 100
    assert pikachu.type == "electric"


def test_tim_collection_dead(my_collection):
    """Check the find_dead method - returns a list"""
    dead = my_collection.find_dead()
    assert type(dead) is list

    # These are the two dead pokemons in our collection
    assert len(dead) == 2
    for pok in dead:
        assert pok.name == "Charizard" or pok.name == "Charmander"
        assert pok.health == 0
