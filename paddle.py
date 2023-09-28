from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xpos = None, ypos = None):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xpos, ypos)

    def up(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def down(self):
        self.goto(self.xcor(), (self.ycor() - 20))