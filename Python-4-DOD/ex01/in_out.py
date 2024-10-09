def square(x: int | float) -> int | float:
    """Returns the square of the argument."""
    if not isinstance(x, (int, float)):
        print("Argument is not a float or an int.")
        return
    else:
        return x * x


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of argument by himself."""
    if not isinstance(x, (int, float)):
        print("Argument is not a float or an int.")
        return
    else:
        return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an object that, when called, returns the result of the
    arguments calculation.
    Args:
        - x (int | float): the number to apply the funtction to.
        - function: the function to apply to the number.
    """
    count = 0

    def inner() -> float:
        """
        Returns the result of the arguments calculation.
        """
        nonlocal x, count
        # nonlocal portée englobante, permet de modifier ds une fonction
        # interne une variable definie dans une fonction externe
        count += 1
        x = function(x)
        return x
    return inner
