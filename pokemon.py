
class Pokemon:
    def __init__(self, name:str, health:int, type:str):
        """Pokemon Class

        Args:
            name (str): name of Pokemon
            health (int): health of pokemon
            type (str): type of pokemon
        """
        self.name = name
        self.health = health
        self.type = type

    def __str__(self):
        """dunder method which returns and f string in format when object is created

        Returns:
            f string
        """
        return f'<{self.name} ({self.type}) - {self.health}HP>'

    def to_dict(self):
        """to dict will create a dictionary of each element so that it is serialized

        Returns:
            dict: dictionary of instance
        """
        return dict(name = self.name, health = self.health, type = self.type)


    def comparison(self):
        """Compares mulitple instances
        """
        pass

