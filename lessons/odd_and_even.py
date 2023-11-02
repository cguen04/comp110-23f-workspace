def odd_and_even(list: list[int]) -> list[int]:
    newlist: list[int] = []
    i = 0
    for num in list:
        if (num % 2 == 1) and (i % 2 == 0):
            newlist.append(list[i])
        i += 1
    return newlist

print(odd_and_even([1, 3, 5, 7]))