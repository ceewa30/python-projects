from turtle import Turtle, Screen
import random
import turtle as t

timmy_the_turtle = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

timmy_the_turtle.shape("turtle")

directions = [0, 90, 180, 270]
num_sides = 200
timmy_the_turtle.pensize(15)

for _ in range(num_sides):
        timmy_the_turtle.speed(10)
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(30)
        timmy_the_turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()