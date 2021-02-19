import turtle
import time
import random
import player
import car

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Naru's turtle crossing")
screen.tracer(0)
screen.listen()

player = player.Player()
car = car.Car()

screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

while True:
    time.sleep(car.car_speed)
    screen.update()

    if player.ycor() > 280:
        player.starting_point()
        car.starting_point()

    for i in car.cars:
        if player.distance(i) < 23:
            player.gameover()

    for i in car.cars:
        if i.xcor() > 290:
            r = random.randint(-200, 200)
            i.goto(-290, r)
        if i.xcor() < -290:
            r = random.randint(-200, 200)
            i.goto(290, r)

    car.move_cars()
