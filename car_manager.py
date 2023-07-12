COLORS=["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random.randint(-250, 250))

    def move(self):
        new_x=self.xcor() - MOVE_INCREMENT
        self.penup()
        self.goto(new_x, self.ycor())


