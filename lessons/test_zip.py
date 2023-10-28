"""Test my zip function."""
___author___ = "730663338"

from lessons.zip import zip
from lessons.zip import fun

def test_zip_len() -> None:
    assert zip(["hello", "world"], [1]) == {}

def test_1_zip() -> None:
    assert zip(["hello"], [1]) == {"hello": 1}


def test_fun() -> None:
    assert fun(2) == 2