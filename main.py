# On Day 20 of the 100 days of code I will be building a version of the classic game snake.
# Built using turtle graphics, feel free to peak around at my code, and play the game!

from turtle import Turtle, Screen
import random
from playsound import playsound

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Classic Snek 🐍")

# Create a row of turtles that act as our snake.
x_coordinates = [0, -20, -40]
turtles = []
for turtle in range(3):
    new_snake_part = Turtle(shape="square")
    new_snake_part.color("white")
    new_snake_part.goto(x=x_coordinates[turtle], y=0)
    turtles.append(new_snake_part)

# TODO: Allow the snake to move.
# TODO: create snake food.
# TODO: Detect collision with food.
# TODO: Create a scoreboard.
# TODO: Detect collision with wall.
# TODO: Detect collision with body or tail.
# TODO: Add music.


screen.exitonclick()