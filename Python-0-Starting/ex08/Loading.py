import sys


def ft_tqdm(lst: range) -> None:
    """
    This function provides a visual progress bar that updates
    in real-time as you iterate over the given range object.
    It uses the `yield` keyword to generate items from the
    input range while displaying the progress bar.

    Parameters:
        lst(range): a range obj representing the sequence of
        items to iterate over. This should be a valid range object,
        e.g., range(10) or range(1, 11).

    Raises:
        TypeError: If the provided argument is not a range object.
    """
    try:
        if not isinstance(lst, range):
            raise TypeError("ft_tqdm() argument must be a range object.")
        try:
            total = len(lst)
        except TypeError:
            raise TypeError("range object must have a defined length.")

        counter = 1
        for item in lst:
            percent_completed = counter / total * 100
            progress_bar_length = 55
            filled_length = int(progress_bar_length * counter / total)
            bar = "█" * filled_length + " " * \
                (progress_bar_length - filled_length)
            sys.stdout.write(f"\r{percent_completed:.0f}%|{bar}| \
                             {counter}/{total}")
            sys.stdout.flush()
            counter += 1
            yield item
        print()

    except TypeError as e:
        print(e)
