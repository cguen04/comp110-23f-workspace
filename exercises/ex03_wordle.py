"""Abstracting Wordle with Functions."""
__author__ = "730663338"


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
    while (i < len(secret)):
        if secret[i] == guess [i]:
            boxes += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
        i += 1
    return boxes

def input_guess(num: int) -> str:
    word = input(f"Enter a { num } character word: ")
    while len(word) != num:
        word = input(f"That wasn't { num } characters! Try again: ")
    return word

def main() -> None:
    """Entry point of program and main game loop."""
    turn = 1
    secret_word = "codes"
    while turn < 7:
        print(f"=== Turn { turn }/6 ===")
        user_guess = input_guess(5)
        print(emojified(secret_word, user_guess))
        if secret_word == user_guess:
            return print(f"You won in { turn }/6 turns!")
        turn += 1
    return print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
