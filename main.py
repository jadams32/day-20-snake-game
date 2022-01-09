# On Day 20 of the 100 days of code I will be building a version of the classic game snake.
# Built using turtle graphics, feel free to peak around at my code, and play the game!

from turtle import Screen
import random
from playsound import playsound
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Classic Snek 🐍")
screen.tracer(0)

# Create a row of turtles that act as our snake.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_right, key="Right")
screen.update()

# TODO: Add music.
playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.start_snake()

    # Check if snake collides with any food on the screen.
    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.update_score()
        snake.ate_food()

    # Check if the snake collides with the horizontal edge of the screen.
    if snake.head.xcor() > 290:
        snake.head.goto(-290, 0)

    if snake.head.xcor() < -290:
        snake.head.goto(290, 0)

    # Check if the snake collides with the vertical edge of the screen.
    if snake.head.ycor() > 290 or snake.head.ycor() < -290:
        playing = False
        scoreboard.game_over()

    # Check if head collides with any part of the snake.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                playing = False
                scoreboard.game_over()

screen.exitonclick()
