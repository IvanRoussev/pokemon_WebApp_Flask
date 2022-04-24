import json
from pokemon import Pokemon

class Collection:
    def __init__(self, name):
        """Collection of pokemons class of name

        Args:
            name (str): name is taken and is used for the path to the json file

        json file is then opened and interpreted. A class instance of Pokemons is made by each value in the Json
        all the different Pokemon instances with different values are then appended to a list called
        self.pokemons
        """
        self.name = name
        self.name = self.name.lower()



        with open(f"data/{self.name}.json", 'r') as fp:
                data = json.load(fp)

        self.pokemons = []
        for item in data['pokemons']:
            self.pokemons.append(
            Pokemon(
            name=item['name'],
            health=item['health'],
            type=item['type']))

        #self.pokemons.sort(key=lambda x: x.health, reverse=True)

    def find_by_name(self, name):
        """this method will find a pokemon by any name you provide and append all matches to a list
        if it is not found in the list with all instances it will return an empty list

        Args:
            name (str): name that is gonna be looking in the list of instances for 

        Returns:
            list which holds all matches of names
        """
        pokemons_found = []
        for pokemons in self.pokemons:
            if pokemons.name.lower() == name.lower():
                pokemons_found.append(pokemons)
        return pokemons_found

    def find_dead(self):
        """finds all dead pokemons, finds them by looking into each instance of pokemons in the list and checks if the attriute has a value of 0
        it then appends all those dead pokemons to a list

        Returns:
            list: returns list of dead pokemons
        """
        dead_pokemons = []
        for items in self.pokemons:
            if items.health == 0:
                dead_pokemons.append(items)
        return dead_pokemons

