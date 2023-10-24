"""Drawing a cabin at night with Turtle. The function that draws trees has been broken up into drawing triangles and a rectangle. I used randint to position and rotate the stars randomly."""
__author__ = "730663338"

from turtle import Turtle, colormode, done
from random import randint


def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float, color: str) -> None:
    """Draws a rectangle horizontally."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color(color)
    a_turtle.begin_fill()
    i: int = 0
    while i < 2:
        a_turtle.forward(length)
        a_turtle.right(90)
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def draw_uprectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float, color: str) -> None:
    """Draws a rectangle but it is oriented vertically."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.left(90)
    i: int = 0
    while i < 2:
        a_turtle.forward(length)
        a_turtle.right(90)
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1
    a_turtle.end_fill()


def draw_star(a_turtle: Turtle, x: float, y: float, length: float, color: str) -> None:
    """Draws a five-pointed star that is randomly oriented."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.right(randint(0, 180))
    i: int = 0
    while i < 5:
        a_turtle.forward(length)
        a_turtle.right(144)
        i += 1
    a_turtle.end_fill()


def draw_triangle(a_turtle: Turtle, x: float, y: float, length: float, color: str) -> None:
    """Draws an equilateral triangle with a flat base."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color(color)
    a_turtle.begin_fill()
    i: int = 0
    a_turtle.left(60)
    while  i < 3:
        a_turtle.forward(length)
        a_turtle.right(120)
        i += 1
    a_turtle.end_fill()


def draw_tree(a_turtle: Turtle, x: float, y: float, length: float, width: float, color1: str, color2: str) -> None:
    """Function that when called will draw a tree. It combines to previous functions"""
    draw_uprectangle(a_turtle, x, y, length, width, color1)
    i = 0
    while i < 3:
        draw_triangle(a_turtle, (x - width * 2), (length + y), (width * 5), color2)
        i += 1
        length += 40


def main() -> None:
    """Where it all comes together."""
    my_turtle: Turtle = Turtle()
    my_turtle.speed(0)
    draw_rectangle(my_turtle, -700, 600, 1500, 1500, "dark green")
    draw_rectangle(my_turtle, -700, 600, 1500, 800, "navy")
    i = 0
    while i < 30:
        draw_star(my_turtle, randint(-600, 600), randint(-175, 500), 30, "yellow")
        i += 1
    i = 0
    xval = -550
    while i < 3:
         draw_tree(my_turtle, xval, -200, 50, 20, "brown", "dark green")
         i += 1
         xval += 130
    draw_rectangle(my_turtle, -150, 0, 300, 200, "brown")
    draw_triangle(my_turtle,-150, 0, 300, "maroon")
    draw_uprectangle(my_turtle, -30, -200, 75, 60, "maroon")
    draw_uprectangle(my_turtle, -100, -100, 50, 50, "yellow")
    draw_uprectangle(my_turtle, 50, -100, 50, 50, "yellow")
    i = 0
    xval = 280
    while i < 3:
         draw_tree(my_turtle, xval, -200, 50, 20, "brown", "dark green")
         i += 1
         xval += 130


main()
done()