"""Summing the elements of a list using different loops."""
__author__ = "730663338"


def w_sum(vals: list[float]) -> float:
    """Getting a sum using a while loop."""
    idx = 0
    sum = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    "Gettin a sum using for... in... without range."
    sum = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    "Getting a sum using for... in... with range."
    sum = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum

