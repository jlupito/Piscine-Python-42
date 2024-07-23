from S1E9 import Character

class Baratheon(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
    
    def __str__(self):
        return f"Baratheon: {self.first_name}, Alive: {self.is_alive}"
    
    def __repr__(self):
        return f"Baratheon('{self.first_name}', {self.is_alive})"
    
    @classmethod
    def create_character(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
    
    def __str__(self):
        return f"Lannister: {self.first_name}, Alive: {self.is_alive}"
    
    def __repr__(self):
        return f"Lannister('{self.first_name}', {self.is_alive})"
    
    @classmethod
    def create_character(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        return Lannister(first_name, is_alive)