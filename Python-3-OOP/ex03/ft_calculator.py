# dunder methods: double underscores methods
class calculator:
    """
    A calculator class that is able to do calculations
    (addition, multiplication, subtraction, division)
    of vector with a scalar.
    Attributes:
        vector (list): The vector on which operations will be performed.
    Methods:
        __init__(self, vector): initializes with the provided vector.
        __add__(self, object): adds scalar to each element of the vector.
        __mul__(self, object): multiplies each element by scalar.
        __sub__(self, object): subtracts scalar from each element.
        __truediv__(self, object): divides each element by scalar.
    """

    def __init__(self, vector):
        """
        initializes with the provided vector.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        adds scalar to each element of the vector.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return None

    def __mul__(self, object) -> None:
        """
        multiplies each element by scalar.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return None

    def __sub__(self, object) -> None:
        """
        subtracts scalar from each element.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return None

    def __truediv__(self, object) -> None:
        """
        divides each element by scalar.
        """
        if object == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
        return None
