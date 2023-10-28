"""Combining two lists into a dictionary."""
___author___ = "730663338"

def zip(keys: list[str], values: list[int]) -> dict[str, int]:
    enddict = dict()
    if len(keys) != len(values):
        return enddict
    idx = 0
    while idx < len(keys):
        enddict[keys[idx]] = values[idx]
        idx += 1
    return enddict

def fun(num) -> int:
    return num