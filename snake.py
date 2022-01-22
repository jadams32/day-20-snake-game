from turtle import Turtle

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for location in COORDINATES:
            self.new_snake_segment(location)

    def new_snake_segment(self, location):
        new_snake_part = Turtle(shape="square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(location)
        self.segments.append(new_snake_part)

    def start_snake(self):
        for num in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[num - 1].xcor()
            y_new = self.segments[num - 1].ycor()
            self.segments[num].goto(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def ate_food(self):
        self.new_snake_segment(self.segments[-1].position())
