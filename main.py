from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time
screen = Screen()
ball = Ball()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
score = Score()
screen.bgcolor("Black")
screen.title("Achintya's Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)
game = True
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
while game:
    time.sleep(ball.bspeed)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.y_bounce()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 45 or ball.xcor() < -320 and ball.distance(l_paddle) < 45:
        ball.x_bounce()
    if ball.xcor() > 380:
        score.lpoint()
        ball.respawn()
    if ball.xcor() < -380:
        score.rpoint()
        ball.respawn()

screen.exitonclick()