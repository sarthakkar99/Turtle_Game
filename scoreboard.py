FONT=("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.level=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.level+=1
        self.hideturtle()
        self.write(self.level, align="center", font=FONT)

    def lose(self):
        self.penup()
        self.goto(0,0)
        self.write("You Lose", align="center", font=FONT)