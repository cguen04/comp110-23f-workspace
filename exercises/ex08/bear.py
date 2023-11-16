"""File to define Bear class."""

class Bear:
    """Bear class."""

    age: int
    hunger_score: int
    
    def __init__(self, begin_age = 0, begin_hunger = 0):
        """Bear constructor."""
        self.age = begin_age
        self.hunger_score = begin_hunger
        return None
    
    def one_day(self):
        """Simulates one bear day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Modifies hunger score of bear."""
        self.hunger_score += num_fish
        return None
    
