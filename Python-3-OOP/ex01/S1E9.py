from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class for a character."""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor method for Character.
        param[0]: first_name (str): The first name of the character.
        param[1]: is_alive (bool, optional): The health state of the character. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method to change the health state of the character.
        """
        pass
    

class Stark(Character):
    """Class representing a Stark character."""
    def __init__(self, first_name, is_alive=True):
        """
        Stark character has been created.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Method to change the health state of a Stark character.
        """
        self.is_alive = False