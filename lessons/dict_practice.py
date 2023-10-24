"""Learning about and practicing dictionaries."""

#create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print("Added mint: ")
print(ice_cream)

#removing key, value pair
ice_cream.pop("mint")
print("Removed mint: ")
print(ice_cream)

#printing a specific value associated with a key
print(f"There are { ice_cream['chocolate'] } orders of chocolate")
#updating a value associated with a key
ice_cream["vanilla"] = 10
print("After updating vanilla: ")
print(ice_cream)

print(f"There are { len(ice_cream) } key-value pairs")

#ice_cream["mint"] = 5
if 'mint' in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint")
else:
    print("No orders of mint")

#using 'for' loop to iterate through dict
for cream in ice_cream:
    print(f"{ cream } has { ice_cream[cream] } orders.")
