# On Day 20 of the 100 days of code I will be building a version of the classic game snake.
# Built using turtle graphics, feel free to peak around at my code, and play the game!

from turtle import Screen
import random
from playsound import playsound
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Classic Snek 🐍")
screen.tracer(0)

# Create a row of turtles that act as our snake.
snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_right, key="Right")
screen.update()


# TODO: If food is collied with make snake longer
# TODO: Create a scoreboard.
# TODO: Detect collision with wall.
# TODO: Detect collision with body or tail.
# TODO: Add music.
playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.start_snake()
    if snake.head.distance(food) < 15:
        food.new_food()


screen.exitonclick()
