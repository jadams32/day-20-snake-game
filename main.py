# On Day 20 of the 100 days of code I will be building a version of the classic game snake.
# Built using turtle graphics, feel free to peak around at my code, and play the game!

from turtle import Turtle, Screen
import random
from playsound import playsound
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Classic Snek 🐍")
screen.tracer(0)

# Create a row of turtles that act as our snake.
x_coordinates = [0, -20, -40]
turtles = []
for turtle in range(3):
    new_snake_part = Turtle(shape="square")
    new_snake_part.color("white")
    new_snake_part.penup()
    new_snake_part.goto(x=x_coordinates[turtle], y=0)
    turtles.append(new_snake_part)

screen.update()

# TODO: create snake food.
# TODO: Detect collision with food.
# TODO: Create a scoreboard.
# TODO: Detect collision with wall.
# TODO: Detect collision with body or tail.
# TODO: Add music.
playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(turtles)-1, 0, -1):
        x_new = turtles[segment - 1].xcor()
        y_new = turtles[segment - 1].ycor()
        turtles[segment].goto(x_new, y_new)
    turtles[0].forward(20)


screen.exitonclick()