from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("ping pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        # Here you can add code to update the score for the left player
        scoreboard.l_point()
    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        # Here you can add code to update the score for the right player
        scoreboard.r_point()
    # End of game loop
    if scoreboard.l_score >= 10 or scoreboard.r_score >= 10:
        is_game_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over", align="center", font=("Courier", 36, "normal"))


screen.exitonclick()


