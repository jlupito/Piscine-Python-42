import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    """
    calculates the BMI of a person based on height and weight.

    Args:
        - height: a list of ints or floats representing the height in cm.
        - weight: a list of ints or floats representing the weight in kg.

    Returns:
        a list of BMI values.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must be of the \
                             same size.")

        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or \
                    not isinstance(w, (int, float)):
                raise TypeError("List elements must be int or float.")
            if h <= 0 or w <= 0:
                raise ValueError("List elements must be positive.")

        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi = weight_array / (height_array ** 2)

        return bmi.tolist()

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if the BMI of a person is above a certain limit.
    Args:
        - bmi: a list of ints or floats representing BMIs.
        - limit: an int which sets the limit.

    Returns:
        A list of booleans with True if above the limit, False if not.
    """
    try:
        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")

        for b in bmi:
            if not isinstance(b, (int, float)):
                raise TypeError("BMI elements must be ints or floats.")

        return [b > limit for b in bmi]

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return
