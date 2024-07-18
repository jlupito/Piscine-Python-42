import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me(list, int, int) -> list

    takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end arguments.
    """
    if not isinstance(family, list):
        raise ValueError("Input must be a list.")
    
    length = None
    for item in family:
        if not isinstance(item, list):
            raise ValueError("All elements of the input must be lists.")
        if length is None:
            length = len(item)
        elif len(item) != length:
            raise ValueError("All lists within the input must be of the same length.")

    array = np.array(family)
    print(f"My shape is : {array.shape}")
    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()