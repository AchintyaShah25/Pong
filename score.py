from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.scorse()


    def scorse(self):
        self.goto(-40, 220)
        self.write(self.lscore, align="center", font=("courier", 60, "normal"))
        self.goto(40, 220)
        self.write(self.rscore, align="center", font=("courier", 60, "normal"))

    def lpoint(self):
        self.lscore +=1
        self.clear()
        self.scorse()

    def rpoint(self):
        self.rscore +=1
        self.clear()
        self.scorse()