"""
---------------------------------------
    * Course: 100 Days of Code - Dra. Angela Yu
    * Author: Noah Louvet
    * Day: 22 - Arcade pong game
    * Subject: Tkinter GUI - OOP
---------------------------------------
"""

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.goto(0, -300)
line.setheading(90)
for _ in range(30):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()


    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x_r_paddle()

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x_l_paddle()

    #Detect a miss
    if ball.xcor() > 375:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
