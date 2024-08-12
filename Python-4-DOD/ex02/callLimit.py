def callLimit(limit: int):
    """
    A decorator generator that takes a limit as an argument and returns a decorator.
    The decorator then limits the number of times a function can be called to this limit.
    :param limit: The maximum number of times the decorated function can be called.
    """
    count = 0
    def callLimiter(function):
        """
        A decorator that limits the number of times a function can be called.
        :param function: The function to be decorated.
        """
        def limit_function(*args: any, **kwds: any):
            """
            A wrapper function that checks if the decorated function has been called
            fewer times than the limit. If so, it calls the function; otherwise, it prints an error.
            :param args: Positional arguments to be passed to the decorated function.
            :param kwds: Keyword arguments to be passed to the decorated function.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {repr(function)} call too many times")
        
        return limit_function
    
    return callLimiter
        
    