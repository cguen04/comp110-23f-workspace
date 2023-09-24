"""Abstracting Wordle with Functions."""
___author___ = "730663338"

def contains_char(str1: str, str2: str) -> bool:
    assert len(str2) == 1
    i = 0
    val = False
    while (i < len(str1)) and (val is False):
        if str1[i] == str2:
            val = True
        i += 1
    if val is True:
        return True
    else:
        return False


    