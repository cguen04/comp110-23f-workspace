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
    assert invert({}) == {}


def test_favorite_color_use_1() -> None:
    """Should return green"""
    assert favorite_color({"John": "green", "Jimmy": "blue", "Cindy": "green"}) == "green"


def test_favorite_color_use_2() -> None:
    """Should return yellow"""
    assert favorite_color({"Greg": "orange", "Lew": "orange", "Veronica": "yellow", "Abed": "yellow", "James": "yellow"}) == "yellow"


def test_favorite_color_edge() -> None:
    """Should return purple. Tests to see how function handles capitalization."""
    assert favorite_color({"Ayden": "gREEN", "Anthony": "pUrpLE", "Jackson": "PURPLE"}) == "purple"


def test_count_use_1() -> None:
    """Should return {"hello": 3, "world": 1}"""
    assert count(["hello", "hello", "hello", "world"]) == {"hello": 3, "world": 1}


def test_count_use_2() -> None:
    """Should return {"my": 1, "name": 1, "is": 1}"""
    assert count(["my", "name", "is"]) == {"my": 1, "name": 1, "is": 1}


def test_count_edge() -> None:
    """Should return {}"""
    assert count([]) == {}

