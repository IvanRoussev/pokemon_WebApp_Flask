from pokemon import Pokemon


def test_pokemon():
    """A Pokemon has a name, health, and type"""
    pikachu = Pokemon(name="Pikachu", health=100, type="electric")
    assert pikachu.name == "Pikachu"
    assert pikachu.health == 100
    assert pikachu.type == "electric"


def test_str():
    """String representation of a Pokemon (dunder)"""
    pikachu = Pokemon(name="Pikachu", health=100, type="electric")
    assert str(pikachu) == "<Pikachu (electric) - 100HP>"


def test_comparison():
    """A given pokemon is "smaller" than another one if their health is "smaller" than the other's"""
    pikachu = Pokemon(name="Pikachu", health=100, type="electric")
    charizard = Pokemon(name="Charizard", health=2, type="flying")

    assert charizard < pikachu


def test_to_dict():
    """Checks a Pokemon can be serialized into a dictionary"""
    pikachu = Pokemon(name="Pikachu", health=100, type="electric")
    assert pikachu.to_dict() == {"name": "Pikachu", "health": 100, "type": "electric"}
