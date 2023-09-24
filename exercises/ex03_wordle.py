"""Abstracting Wordle with Functions."""
___author___ = "730663338"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

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

def emojified(secret: str, guess: str) -> str:
    assert len(secret) == len(guess)
    boxes = ""
    i = 0
    while (1 < len(secret)):
        if secret[i] == guess [i]:
            boxes += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
    return boxes
