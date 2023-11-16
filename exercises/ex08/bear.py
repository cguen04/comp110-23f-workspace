"""File to define Bear class"""

class Bear:

    age: int
    hunger_score: int
    
    def __init__(self, begin_age = 0, begin_hunger = 0):
        self.age = begin_age
        self.hunger_score = begin_hunger
        return None
    
    def one_day(self):
        return None