from turtle import Turtle
ALIGNMENT = "center"
FONT_STYLE = ('Chalkboard', 28, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.initial_score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.write_to_screen()

    def update_score(self):
        self.initial_score += 1
        self.write_to_screen()

    def write_to_screen(self):
        self.clear()
        self.write(f"Score: {self.initial_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT_STYLE)

    def reset_score(self):
        if self.initial_score > int(self.high_score):
            self.high_score = self.initial_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.initial_score = 0
        self.write_to_screen()

