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
    color_dict_vals: dict[str, int] = {}
    color_list: list[str] = []
    for name in colors:
        color_list.append(colors[name])
    for color in color_list:
        i = 0
        counter = 0
        while i < len(color_list):
            if color == color_list[i]:
                counter += 1
            i += 1
        color_dict_vals[color] = counter
    max_color = 0
    for color in color_dict_vals:
        if color_dict_vals[color] > max_color:
            max_color = color_dict_vals[color]
    for color in color_dict_vals:
        if max_color == color_dict_vals[color]:
            return color


def count(list_in: list[str]) -> dict[str, int]:
    dict_out: dict[str, int] = {}
    for val in list_in:
        if val in dict_out:
            dict_out[val] += 1
        if val not in dict_out:
            dict_out[val] = 1
    return dict_out

def alphabetizer(list_in: list[str]) -> dict[str, list[str]]:
    