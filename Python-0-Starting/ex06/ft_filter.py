def ft_filter(function_to_apply, iterable):
    """
    Filters the given sequence with the help of a function
    that tests each element in the sequence to be true or not.

    Args:
        - function_to_apply: A Function to be run for each item
        in the iterable.
        - iterable: The iterable to be filtered.

    Returns:
        An list filtered.
    """
    if function_to_apply is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function_to_apply(item)]


def main():

    numbers = range(-10, 10)

    pos_nb_ft = ft_filter(lambda x: x > 0, numbers)
    print(list(pos_nb_ft))

    pos_nb = filter(lambda x: x > 0, numbers)
    print(list(pos_nb))

    print(filter.__doc__)
    print(ft_filter.__doc__)


if __name__ == "__main__":
    main()
