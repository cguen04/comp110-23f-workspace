"""Dictionary functions."""
__author__ = "730663338"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dict."""
    dict2: dict[str, str] = {}
    new_keys: list[str] = []
    for key in dict1:
        new_keys.append(dict1[key])
        dict2[dict1[key]] = key
    idx = 1
    i = 1
    for val in new_keys:
        while i < len(new_keys):
            if val == new_keys[i]:
                raise KeyError("identical keys")
            i += 1
        idx += 1
        i = idx
    return dict2


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color most often said to be the favorite."""
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
    """Counts how many times an item appears in a list and returns a dict with the item as the key and the frequency as the value."""
    dict_out: dict[str, int] = {}
    for val in list_in:
        if val in dict_out:
            dict_out[val] += 1
        if val not in dict_out:
            dict_out[val] = 1
    return dict_out


def alphabetizer(list_in: list[str]) -> dict[str, list[str]]:
    """Takes a list of items and returns a dictionary with the items sorted by the first character."""
    dict_out: dict[str, list[str]] = {}
    for elem in list_in:
        x = ""
        x = elem[0].lower()
        dict_out[x] = []
    for key in dict_out:
        for elem in list_in:
            if key == elem[0].lower():
                dict_out[key] += [elem]
    return dict_out


def update_attendance(dict_in: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Takes an existing dictionary and updates it with new values."""
    if day in dict_in:
        dict_in[day] += [student]
    if day not in dict_in:
        dict_in[day] = [student]
    return dict_in
