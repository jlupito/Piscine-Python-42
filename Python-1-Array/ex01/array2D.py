import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of an array and truncates it based on given
    start and end.
    Args:
        - family (list): the 2D array.
        - start (int): the start index for truncation.
        - end (int): the end index for truncation.

    Returns:
        A 2D list truncated.
    """
    try:
        if not isinstance(family, list):
            raise ValueError("Input must be a list.")

        if not all(isinstance(element, list) for element in family):
            raise TypeError("All elements of the input must be lists.")

        for element in family:
            if not all(isinstance(sub_element, (int, float)) for sub_element
                       in element):
                raise TypeError("All sub_elements of the family elements \
                                must be int or float.")

        length = len(family[0])
        if not all(len(element) == length for element in family):
            raise ValueError("All lists must have the same length.")

        array = np.array(family)
        print(f"My shape is : {array.shape}")
        new_array = array[start:end]
        print(f"My new shape is : {new_array.shape}")
        return new_array.tolist()

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return
