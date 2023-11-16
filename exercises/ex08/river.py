"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_bear: list[Bear] = self.bears
        for bear in new_bear:
            if bear.age > 5:
                new_bear.pop()
        new_fish: list[Fish] = self.fish
        for fish in new_fish:
            if fish.age > 3:
                new_fish.pop()
        self.bears = new_bear
        self.fish = new_fish 
        return None
    
    def remove_fish(self, amount: int):
        x = amount
        while x >=0:
            self.fish.pop(0)
            x -= 1
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        for bear in self.bears:
            if bear.hunger_score() < 0:
                self.bears.pop()
        return None
        
    def repopulate_fish(self):
        x = 4(len(self.fish)//2)
        while x > 0:
            self.fish.append(Fish)
            x -=1
        return None
    
    def repopulate_bears(self):
        x = len(self.bears)//2
        while x > 0:
            self.bears.append(Bear)
            x -= 1
        return None
    
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        idx = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
        return None
    
