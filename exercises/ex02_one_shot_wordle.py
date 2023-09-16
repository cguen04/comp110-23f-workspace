"""Continuing to work towards Wordle."""
___author___ = "730663338"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#copy and pasted from ex02 instructions
secret: str = "python"
guess: str = input(f"What is your { len(secret) }-letter guess? ")
while len(guess) != len(secret):
    guess = input(f"That was not { len(secret) } letters! Try again: ")
counter = 0
boxes = ""
while counter < len(secret):
    if guess[counter] == secret[counter]:
        boxes += GREEN_BOX
    else:
        ind = 0
        val = False
        while val == False and ind < len(secret):
            if guess[counter] == secret[ind]:
                val = True
            else:
                ind += 1
        if val == True:
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
    counter += 1
print(boxes)
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
