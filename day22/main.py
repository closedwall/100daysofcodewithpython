from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import math
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_spped)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_paddle)< 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_spped*=0.9


    if ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()