"""Testing dict funcitons."""
__author__ = "730663338"

import pytest
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


def test_invert_use_1() -> None:
    """Should return {"world": "hello", "meatballs": "spaghetti"}"""
    assert invert({"hello": "world", "spaghetti": "meatballs"}) == {"world": "hello", "meatballs": "spaghetti"}


def test_invert_use_2() -> None:
    """Should return {"b": "a", "d": "c", "f": "e", "h": "g", "j": "i", "l": "k"}"""
    assert invert({"a": "b", "c": "d", "e": "f", "g": "h", "i": "j", "k": "l"}) == {"b": "a", "d": "c", "f": "e", "h": "g", "j": "i", "l": "k"}


def test_invert_edge() -> None:
    """Should return {}"""
    assert invert() == {}

