import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    give_bmi(list[int | float], list[int | float]) -> list[int | float]

    takes 2 lists of integers or floats in input and returns a list
    of BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same size.")

    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Height list elements must be int or float.")
    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("Weight list elements must be int or float.")

    height_cm = np.array(height) 
    weight_kg = np.array(weight)
    bmi_values = weight_kg / (height_cm ** 2)

    return list(bmi_values)

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit(list[int | float], int) -> list[bool]

    accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans (True if above the limit).
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI list elements must be int or float.")

    return [b > limit for b in bmi]
