"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    def __init__(self, in_list: list[float]) -> None:
        self.values = in_list
        return None


    def __str__(self) -> str:
        return f"Simpy({self.values})"


    def fill(self, float: float, int: int) -> None:
        new_list = []
        for num in range(int):
            new_list.append(float)
        self.values = new_list
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        new_list = []
        assert step != 0.0
        if step > 0:
            while start < stop:
                new_list.append(start)
                start += step
        else:
            while start > stop:
                new_list.append(start)
                start += step
        self.values = new_list
        return None
    

    def sum(self) -> float:
        return sum(self.values)
    

    def __add__(self, right_hand: float | Simpy) -> Simpy:
        new_simpy: Simpy = Simpy([])
        list_right: list[float] = []
        if type(right_hand) is float:
            for num in range(len(self)):
                list_right.append(self.values[num] + right_hand)
            new_simpy.values = list_right
        elif type(right_hand) is Simpy:
            assert len(self) == len(right_hand)
            for num in range(len(self)):
                list_right.append(self.values[num] + right_hand[num])
            new_simpy.values = list_right
        return new_simpy
    



