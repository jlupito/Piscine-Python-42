import sys

def ft_filter(function_to_apply, iterable):
    """
    ft_filter(function or None, iterable) --> ft_filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function_to_apply is None:
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function_to_apply(item))

def main():


    # ATTENTION, FAIRE UN MINIMUM DE PARSING DES ARGUMENTS
    # ET PASSER L EXEMPLE EN SYS ARGV
    numbers = range(-10, 10)

    pos_nb_ft = ft_filter(lambda x: x > 0, numbers)
    print(list(pos_nb_ft))

    pos_nb = filter(lambda x: x > 0, numbers)
    print(list(pos_nb))

    print(filter.__doc__)
    print(ft_filter.__doc__)

if __name__ == "__main__":
    main()