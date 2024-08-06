from turtle import Turtle
from ball import Ball


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)

    def go_right(self):
        if self.xcor() <= 340:
            self.goto(self.xcor() + 8,self.ycor())

    def go_left(self):
        if self.xcor() >= -360:
            self.goto(self.xcor() - 8,self.ycor())

    def space(self):
        self.ball.move()
