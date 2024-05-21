from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

colors = ["dark green", "light blue", "maroon", "dark slate blue", "magenta"]
num_sides = 3

while num_sides < 11:
    angle = 360 / num_sides
    for i in range(num_sides):
        timmy_the_turtle.speed(1)
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)
    if i == num_sides - 1:
        num_sides += 1
        timmy_the_turtle.color(random.choice(colors))

screen = Screen()
screen.exitonclick()