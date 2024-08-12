def square(x: int | float) -> int | float:
    """returns the square of the argument"""
    if not isinstance(x, (int, float)):
        print(f"{x} is not a float or an int")
        return
    else:
        return x * x

def pow(x: int | float) -> int | float:
    """returns the exponentiation of argument by himself"""
    if not isinstance(x, (int, float)):
        print(f"{x} is not a float or an int")
        return
    else:
        return x ** x

def outer(x: int | float, function) -> object:
    """
    returns an object that when called returns the result of the arguments
    calculation
    """
    count = 0
    def inner() -> float:
        """
        returns the result of the arguments calculation
        """
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    return inner