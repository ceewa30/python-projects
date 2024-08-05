from turtle import Turtle, Screen
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-140, -80, -20, 20, 80, 140]
all_turtles = []

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        for self.turtle_index in range(0, random.randint(1, 6)):
            self.new_turtle = Turtle(shape="square")
            self.new_turtle.penup()
            self.new_turtle.color(colors[self.turtle_index])
            self.new_turtle.goto(x=-230, y=y_positions[self.turtle_index])
            self.new_turtle.shapesize(stretch_wid=1, stretch_len=3)
            all_turtles.append(self.new_turtle)