# On Day 20 of the 100 days of code I will be building a version of the classic game snake.
# Built using turtle graphics, feel free to peak around at my code, and play the game!

from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor("black")

john = Turtle(shape="square")
john.color("white")


screen.exitonclick()