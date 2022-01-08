from turtle import Turtle

X_COORDINATES = [0, -20, -40]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()

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
        self.turtles[0].forward(MOVE_DISTANCE)
    def up(self):
        self.turtles[0].setheading(90)

    def down(self):
        self.turtles[0].setheading(270)

    def turn_left(self):
        self.turtles[0].setheading(180)

    def turn_right(self):
        self.turtles[0].setheading(0)
