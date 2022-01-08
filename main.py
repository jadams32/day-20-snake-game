# On Day 20 of the 100 days of code I will be building a version of the classic game snake.
# Built using turtle graphics, feel free to peak around at my code, and play the game!

from turtle import Turtle, Screen
import random
from playsound import playsound
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Classic Snek 🐍")
screen.tracer(0)

# Create a row of turtles that act as our snake.
snake = Snake()
new_snake = snake.create_snake()
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
    snake.start_snake(new_snake)


screen.exitonclick()
