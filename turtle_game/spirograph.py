from turtle import Turtle, Screen
import random
import turtle as t

timmy_the_turtle = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

timmy_the_turtle.shape("arrow")
timmy_the_turtle.speed(0)

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
        # timmy_the_turtle.left(i + 2)

draw_spirograph(5)



screen = Screen()
screen.exitonclick()