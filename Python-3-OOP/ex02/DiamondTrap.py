from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the false King."""
    def __init__(self, first_name, is_alive=True):
        """Method to initialize the false King."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Method to set the eyes color of the false King."""
        self.eyes = color

    def set_hairs(self, color):
        """Method to set the hairs color of the false King."""
        self.hairs = color

    def get_eyes(self):
        """Method to get the eyes color of the false King."""
        return self.eyes

    def get_hairs(self):
        """Method to get the hairs color of the false King."""
        return self.hairs
