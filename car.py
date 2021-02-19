from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'grey', 'gold', 'pink']
FONT = ('courier', 20, 'normal')

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.write(f"Level = {self.level}", align='center', font=FONT)
        self.car_speed = 0.1
        self.starting_cars(10)

    def starting_cars(self, n):
        self.clear()
        self.write(f"Level = {self.level}", align='center', font=FONT)

        for i in range(0, n):
            r = random.randint(-200,200)
            t = Turtle('square')
            t.shapesize(1, 2)
            t.color(random.choice(COLORS))
            t.setheading(180)
            t.penup()
            t.goto(280, r)
            self.cars.append(t)

        for i in range(0, n):
            r = random.randint(-200,200)
            t = Turtle('square')
            t.shapesize(1, 2)
            t.color(random.choice(COLORS))
            t.penup()
            t.goto(-280, r)
            self.cars.append(t)

    def move_cars(self):
        for i in self.cars:
            r= random.randint(0,10)
            i.penup()
            i.forward(r)

    def starting_point(self):
        for i in self.cars:
            i.hideturtle()
        self.cars = []
        self.car_speed *= 0.9
        self.level += 1
        self.starting_cars(10)