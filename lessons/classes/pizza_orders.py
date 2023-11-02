"""Instantiating a class."""

"""
This is where we instantiate the class 
we defined in classes.py.
In other words, we're creating objects 
that belong to that class.
"""

# import the class
# from <file_name>.<module_name> import <class>
from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("large", 10, True) # constructor
# access/set/update attribute values
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

print("Size: ")
print(my_pizza.size)

print("my_pizza: ")
print(my_pizza)