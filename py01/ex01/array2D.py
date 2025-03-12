import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Truncate a 2D array and print its shape.

This function accepts a 2D array (a list of lists) along with start
and end indices.
It first verifies that the input is a valid 2D array where each
inner list has the same length.
Then, it prints the shape of the array (number of rows and number of columns)
and returns a new
2D array in which each inner list has been sliced using Python’s
slicing syntax (from 'start'
index (inclusive) to 'end' index (exclusive))."""
    try:
        assert isinstance(family, list), "Family not list"
    except AssertionError as e:
        print("AssertionError:", e)
        exit(1)
    for listt in family:
        try:
            assert isinstance(listt, list), "Contents not list"
        except AssertionError as e:
            print("AssertionError:", e)
            exit(1)
    leg = len(family[0])
    for row in family:
        try:
            assert leg == len(row), "Not equal Length"
        except AssertionError as e:
            print("AssertionError:", e)
            exit(1)
    try:
        arr = np.array(family)
    except Exception as e:
        raise TypeError("Cannot be converted toa NumPy array: " + str(e))
        exit(1)
    if not isinstance(start, int):
        raise TypeError("Invalid start: must be an integer.")
    if not isinstance(end, int):
        raise TypeError("Invalid end: must be an integer.")
    print("My shape is:", arr.shape)
    new_arr = arr[start:end]
    print("My new shape is:", new_arr.shape)
    return new_arr.tolist()
