from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

score = Score()

p2 = Paddle()
p2.goto(350,0)

p1 = Paddle()
p1.goto(-350,0)

ball = Ball()



screen.listen()
screen.onkey(p2.up,"Up")
screen.onkey(p2.down,"Down")
screen.onkey(p1.up,"w")
screen.onkey(p1.down,"s")

speed = 0.1
game = True
while game:

    time.sleep(speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        speed -= 0.005

    if ball.distance(p1) < 50 and ball.xcor() > -330:
        ball.bounce_x()
        speed -= 0.005

    if ball.distance(p2) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        speed -= 0.005

    if ball.xcor() > 390:
        score.increase_1()
        ball.reset()
        speed = 0.1

    if ball.xcor() < -390:
        score.increase_2()
        ball.reset()
        speed = 0.1

    if score.s1 >= 3 or score.s2 >= 3:
        score.game_over()
        game = False



screen.exitonclick()

