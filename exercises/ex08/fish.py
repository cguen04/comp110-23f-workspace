"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self, begin_age=0):
        """Fish constructor."""
        self.age = begin_age
        return None
    
    def one_day(self):
        """Simulates one fish day."""
        self.age += 1
        return None