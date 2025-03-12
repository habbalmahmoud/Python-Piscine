def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the Body Mass Index (BMI) for
        corresponding pairs of weights and heights.

The BMI is defined as the weight (in kilograms) divided by
the square of the height (in meters):

BMI = weight / (height ** 2)

Parameters:
weights (list of int or float): A list of weights in kilograms.
heights (list of int or float): A list of heights in meters.

Returns:
    list of float: A list containing the BMI value for each
    pair of weight and height.

Raises:
    ValueError: If the lengths of the weights and heights lists do not match.
    ZeroDivisionError: If any height is zero (to avoid division by zero).

Example:
    >>> weights = [70, 80, 60]
    >>> heights = [1.75, 1.8, 1.65]
    >>> give_bmi(weights, heights)
    [22.857142857142858, 24.691358024691358, 22.03856749311295]"""
    try:
        assert len(height) == len(weight), "Invalid Input"
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    for s in height:
        try:
            assert isinstance(s, (int, float)) and s != 0, "Invalid type"
        except AssertionError as e:
            print("AssertionError:", e)
            exit(1)
    for s in weight:
        try:
            assert isinstance(s, (int, float)) and s != 0, "Invalid type"
        except AssertionError as e:
            print("AssertionError:", e)
            exit(1)
    bmi_list = list([])
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        bmi_list.append(bmi)
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Evaluate each element in a list of numbers to
    determine if it exceeds a given limit.

Parameters:
numbers (list of int or float): A list containing numeric values.
limit (int): An integer representing the threshold value.
Each number in the list is compared to this limit.

Returns:
    list of bool: A list of booleans where each element is True if the
    corresponding number in 'numbers' is greater than 'limit', and False
    otherwise.

Example:
    >>> apply_limit([3, 7, 10, 2, 5], 5)
    [False, True, True, False, False]"""
    try:
        assert len(bmi) > 0, "Invalid BMI"
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    try:
        assert type(limit) is int, "Limit must be an Integer"
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    for s in bmi:
        try:
            assert isinstance(s, (int, float)), "Bmi Error"
        except AssertionError as e:
            print("AssertionError:", e)
            exit(1)
    return [num > limit for num in bmi]
