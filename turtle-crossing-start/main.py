from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle running game")
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-140, -80, -20, 20, 80, 140]
all_turtles = []
screen.tracer(0)

def car():
    for turtle_index in range(0, random.randint(1, 6)):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()

        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        new_turtle.shapesize(stretch_wid=1, stretch_len=3)
        all_turtles.append(new_turtle)
        screen.update()

# if user_bet:
car()
is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            car()
            winning_color = turtle.pencolor()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
