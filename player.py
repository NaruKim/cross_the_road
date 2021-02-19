import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

    def starting_point(self):
        self.goto(0, -280)

    def gameover(self):
        t = turtle.Turtle()
        t.reset()
        t.write("Game Over", align='center', font=('courier',30,'normal'))
        turtle.Screen().exitonclick()