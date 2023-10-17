"""Turtle Tutorial."""
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-100, 75)
leo.pendown()
leo.color(97, 4, 255)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.right(120)
    i += 1
leo.end_fill()

done()