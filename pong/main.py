from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, 's')
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() >= 295 or ball.ycor() <= -295:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
    if ball.xcor() > 400:
        ball.reverse_position()
        scoreboard.l_point()
    if ball.xcor() < -400:
        ball.reverse_position()
        scoreboard.r_point()

screen.exitonclick()
