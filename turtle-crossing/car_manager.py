from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        self.random_chance = random.randint(1,6)
        if self.random_chance == 1:
            self.new_car = Turtle(shape="square")
            self.new_car.shapesize(stretch_wid=1, stretch_len=2, outline=1)
            self.new_car.penup()
            self.new_car.color(random.choice(COLORS))
            self.new_car.goto(300, y=random.randint(-250, 250))
            self.all_cars.append(self.new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT