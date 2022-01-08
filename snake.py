from turtle import Turtle

X_COORDINATES = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for turtle in range(3):
            new_snake_part = Turtle(shape="square")
            new_snake_part.color("white")
            new_snake_part.penup()
            new_snake_part.goto(x=X_COORDINATES[turtle], y=0)
            self.turtles.append(new_snake_part)

    def start_snake(self):
        for segment in range(len(self.turtles) - 1, 0, -1):
            x_new = self.turtles[segment - 1].xcor()
            y_new = self.turtles[segment - 1].ycor()
            self.turtles[segment].goto(x_new, y_new)
        self.head.forward(MOVE_DISTANCE)

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
