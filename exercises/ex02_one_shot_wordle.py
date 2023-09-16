"""Continuing to work towards Wordle."""
__author__:  str = "730663338"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# copy and pasted from ex02 instructions
secret: str = "python"
guess: str = input(f"What is your { len(secret) }-letter guess? ")
while len(guess) != len(secret):
    guess = input(f"That was not { len(secret) } letters! Try again: ")
counter = 0
boxes = ""
while counter < len(secret):
    if guess[counter] == secret[counter]:
        boxes += GREEN_BOX
        # if guess and secret have the same character at the same index, green box is concatenated
    else:
        ind = 0
        val = False
        # variables testing for 'yellow boxes' are initiated
        while val is False and ind < len(secret):
            if guess[counter] == secret[ind]:
                val = True
                # if guess matches secret at another index, val is set to True which will concatenate a yellow box
            else:
                ind += 1
                # if no match is found at the index being tested, the next index of the secret word is checked
        if val is True:
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
            # white box is concatenated if val == False; guess was not found at any of the indices of secret
    counter += 1
print(boxes)
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
