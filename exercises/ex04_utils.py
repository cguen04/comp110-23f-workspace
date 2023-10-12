"""List utility functions."""
__author__ = "730663338"


def all(input: list[int], x: int) -> bool:
    """Returns True if all ints in the list are the same."""
    if len(input) <= 0:
        return False
    i = 0
    while len(input) > i:
        if input[i] == x:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the highest value in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    if len(input) == 1:
        return input[0]
    i = 1
    x = input[0]
    while len(input) > i:
        if x < input[i]:
            x = input[i]
        i += 1
    return x


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Returns True if both values at each index in both lists are equal."""
    if len(input1) != len(input2):
        return False
    i = 0
    while (len(input1) and len(input2)) > i:
        if input1[i] != input2[i]:
            return False
        i += 1
    return True