from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.initial_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.write_to_screen()

    def update_score(self):
        self.initial_score += 1
        self.clear()
        self.write_to_screen()

    def write_to_screen(self):
        self.write(f"Score: {self.initial_score}", move=False, align='center', font=('Arial', 28, 'normal'))