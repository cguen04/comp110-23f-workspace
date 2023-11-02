"""Defining a class."""


"""
Think of a class definition as a "roadmap"
for objects that belong 
to the class
You are defining the underlying structure
every instance of this class will have
"""

class Pizza:
    """This is my class to represent pizza."""

    # attributes
    # syntax <name> : <type> 
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        """Constructor"""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        # returns self
    
    def price(self) -> float:
        """Method to compute price of pizza."""
        if self.size == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost


