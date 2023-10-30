"""Dictionary functions."""
__author__ = "730663338"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    dict2: dict[str, str] = {}
    new_keys: list[str] = []
    for key in dict1:
        new_keys.append(dict1[key])
        dict2[dict1[key]] = key
    idx = 1
    i = 1
    for str in new_keys:
        while i < len(new_keys):
            if str == new_keys[i]:
                raise KeyError("identical keys")
            i += 1
        idx += 1
        i = idx
    return dict2


def favorite_color(colors:dict[str, str]) -> str:
    colors_list =[]



print(invert({"a": "wod", "b": "wod", "c": "world"}))
