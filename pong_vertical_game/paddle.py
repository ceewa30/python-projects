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
        x = self.xcor()
        x += 20
        self.setx(x)
        print(x)
        right_key = True
        while right_key:
            if x == 360 and self.xcor() == 360:
                print("you reached right")
                right_key = False

    def go_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)
        if self.xcor() == -360:
            print("you reached")

    def space(self):
        self.ball.move()
