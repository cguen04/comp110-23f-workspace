"""ex01 - Chardle - working towards Wordle"""
__author__="730663338"


five_chr_word: str = input("Enter a 5-character word: ")
if len(five_chr_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
one_chr: str = input("Enter a single character: ")
if len(one_chr) != 1:
    print("Error: Character must be a single character.")
    exit()
counter: int = 0
print("Searching for " + one_chr + " in " + five_chr_word)
if five_chr_word[0] == one_chr:
    print(one_chr+" found at index 0")
    counter += 1
if five_chr_word[1] == one_chr:
    print(one_chr+" found at index 1")
    counter += 1
if five_chr_word[2] == one_chr:
    print(one_chr+" found at index 2")
    counter += 1
if five_chr_word[3] == one_chr:
    print(one_chr+" found at index 3")
    counter += 1
if five_chr_word[4] == one_chr:
    print(one_chr+" found at index 4")
    counter += 1
#a loop would have made this simpler but instructions seemed like a loop was not wanted
if counter == 0:
    print("No instances of " + one_chr + " found in " + five_chr_word)
elif counter == 1:
    print("1 instance of " + one_chr + " found in " + five_chr_word)
else:
    print(str(counter) + " eeinstances of " + one_chr + " found in " + five_chr_word)



