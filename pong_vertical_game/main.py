from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong Vertical")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle = Paddle()
ball = Ball()


screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

def resume():
    screen.goto(-100, 260)
    screen.write("Team A ", align="center", font=("Courier", 24, "normal"))

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall y-axis
    if ball.ycor() > 280:
        ball.y_bounce()

    # Detect collision with wall in x-axis
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.x_bounce()

    # Detect collision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() < -50:
        ball.y_bounce()

    # Detect paddle misses
    if ball.ycor() < -300:
        screen.onkey(ball.reset_position, "space")



screen.exitonclick()