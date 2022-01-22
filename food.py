from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=.8, stretch_wid=.8)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 250)
        self.goto(rand_x, rand_y)