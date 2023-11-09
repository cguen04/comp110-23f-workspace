from __future__ import annotations
"""Making Point class."""
__author__ = "730663338"


class Point:
    """Point class."""

    # attrbutes
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> Point:
        """Mutates a Point."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Creates a new Point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Prints out a legible representation of Point."""
        out = f"x: {self.x}; y: {self.y}"
        return out
    
    def __mul__(self, factor: int|float) -> Point:
        """Making a new Point with multiplication."""
        point_out: Point = Point(self.x * factor, self.y * factor)
        return point_out
    
    def __add__(self, addend: int|float) -> Point:
        """Making a new Point with add."""
        point_out: Point = Point(self.x + addend, self.y + addend)
        return point_out
    

