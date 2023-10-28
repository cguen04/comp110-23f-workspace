"""Test my zip function."""
___author___ = "730663338"


from lessons.zip import zip


def test_zip_len() -> None:
    """Function zip with two lists of unequal length should return an empty list."""
    assert zip(["hello", "world"], [1]) == {}


def test_1_zip() -> None:
    """Function zip(["hello"], [1]) == {"hello": 1}."""
    assert zip(["hello"], [1]) == {"hello": 1}


def test_zip_lists() -> None:
    """Function zip(["a", "b", "c", "d"], [1, 2, 3, 4] == {"a": 1, "b": 2, "c": 3, "d": 4})."""
    list1 = ["a", "b", "c", "d"]
    list2 = [1, 2, 3, 4]
    assert zip(list1, list2) == {"a": 1, "b": 2, "c": 3, "d": 4}
