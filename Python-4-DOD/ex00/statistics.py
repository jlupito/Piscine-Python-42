
def calculate_mean(list):
    """
    calculates the mean of a list of numbers.
    """
    if len(list) == 0:
        return None
    return sum(list) / len(list)

def calculate_median(list):
    """
    calculates the median of a list of numbers.
    """
    if len(list) == 0:
        return None
    list.sort()
    length = len(list)
    if  length % 2 == 0:
        return (list[int(length/2) - 1] + list[int(length/2)]) / 2
    else:
        return list[int(length/2)]

def calculate_quart(list):
    """
    calculates the quartile (25% and 75%) of a list of numbers.
    """
    if len(list) == 0:
        return None
    list.sort()
    length = len(list)
    half = int(length / 2)

    if length % 2 == 0:
        Q1 = calculate_median(list[:half])
        Q3 = calculate_median(list[half:])
    else:
        Q1 = calculate_median(list[:half])
        Q3 = calculate_median(list[half + 1:])

    return Q1, Q3

def calculate_std_var(list, flag):
    """
    calculates the Standard Deviation of a list of numbers.
    """
    # La variance est la moyenne des carrés des différences entre chaque élément et la moyenne.
    # l'écart-type est la racine carrée de la variance.
    
    if len(list) == 0:
        return None
    mean = calculate_mean(list)
    var = sum((x - mean) ** 2 for x in list) / len(list)
    std = var ** 0.5
    if flag == 0:
        return std
    else:
        return var

def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    ft_statistics(*args: Any, **kwargs: Any) -> None
    takes in *args a quantity of unknown number and make the Mean, Median,
    Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
    ask.
    """

    list = []
    for arg in args:
        if isinstance(arg, (int, float)):
            list.append(arg)
    for key, value in kwargs.items():
        if value.lower() == "mean":
            result = calculate_mean(list)
        elif value.lower() == "median":
            result = calculate_median(list)
        elif value.lower() == "quartile":
            result = calculate_quart(list)
        elif value.lower() == "std":
            result = calculate_std_var(list, 0)
        elif value.lower() == "var":
            result = calculate_std_var(list, 1)
        else:
            return None
        if result is not None:
            print(f"{value.lower()}: {result}")
        else:
            print("ERROR")