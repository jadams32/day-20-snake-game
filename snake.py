from turtle import Turtle


class Snake:

    def create_snake(self):
        turtles = []
        x_coordinates = [0, -20, -40]
        for turtle in range(3):
            new_snake_part = Turtle(shape="square")
            new_snake_part.color("white")
            new_snake_part.penup()
            new_snake_part.goto(x=x_coordinates[turtle], y=0)
            turtles.append(new_snake_part)
        return turtles

    def start_snake(self, turtles):
        for segment in range(len(turtles) - 1, 0, -1):
            x_new = turtles[segment - 1].xcor()
            y_new = turtles[segment - 1].ycor()
            turtles[segment].goto(x_new, y_new)
        turtles[0].forward(20)
