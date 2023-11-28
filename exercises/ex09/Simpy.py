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
