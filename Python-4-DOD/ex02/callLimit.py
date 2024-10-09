# Un décorateur est une fonction qui permet de modifier
# ou d'étendre le comportement d'une autre fonction ou méthode
# sans changer son code source.
def callLimit(limit: int):
    """
    A decorator generator that takes a limit as an argument
    and returns a decorator.
    Args:
        limit (int): The maximum number of times the decorated
        function can be called.
    """

    def callLimiter(function):
        """
        A decorator that limits the number of times a function
        can be called.
        Args:
            function: The function to be decorated.
        """
        count = 0

        def limit_function(*args: any, **kwargs: any):
            """
            A wrapper function that checks if the decorated function
            has been called fewer times than the limit. If so, it
            calls the function; otherwise, it prints an error.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {repr(function)} call too many times")

        return limit_function

    return callLimiter
