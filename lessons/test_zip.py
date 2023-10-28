"""Test my zip function."""
___author___ = "730663338"

from lessons.zip import zip

def test_zip_len() -> None:
    assert zip(["hello", "world"], [1]) == {}


def test_1_zip() -> None:
    assert zip(["hello"], [1]) == {"hello": 1}


def test_zip_lists() -> None:
    list1 = ["a", "b", "c", "d"]
    list2 = [1, 2, 3, 4]
    assert zip(list1, list2) == {"a": 1, "b": 2, "c": 3, "d": 4}
