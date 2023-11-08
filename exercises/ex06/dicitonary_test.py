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

