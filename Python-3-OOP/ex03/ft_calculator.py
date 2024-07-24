class calculator:
    """
    A calculator class that is able to do calculations (addition, multiplication, sub-
    traction, division) of vector with a scalar.
    Attributes:
        vector (list): The vector on which operations will be performed.
    Methods:
        __init__(self, vector): initializes with the provided vector.
        __add__(self, object): adds object/value to each element of the vector.
        __mul__(self, object): multiplies each element by object/value.
        __sub__(self, object): subtracts object/value from each element.
        __truediv__(self, object): divides each element by object/value.
    """

    def __init__(self, vector):
        """
        __init__(self, vector)
        initializes with the provided vector.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        __add__(self, object)
        adds object/value to each element of the vector.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return None

    def __mul__(self, object) -> None:
        """
        __mul__(self, object)
        multiplies each element by object/value.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return None

    def __sub__(self, object) -> None:
        """
        __sub__(self, object)
        subtracts object/value from each element.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return None

    def __truediv__(self, object) -> None:
        """
        __truediv__(self, object)
        divides each element by object/value.
        """
        if object == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
        return None