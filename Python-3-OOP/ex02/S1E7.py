from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Method to initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method to change the health state of a Baratheon."""
        self.is_alive = False
    
    def __str__(self):
        """Human-readable method to represent the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Special method to represent the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    @classmethod
    def create_character(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Method to initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    
    def __str__(self):
        """Human-readable method to represent the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Special method to represent the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    def die(self):
        """Method to change the health state of a Lannister."""
        self.is_alive = False
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister character instance with custom is_alive status."""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance

