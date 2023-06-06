from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()




    def up(self):
        new = self.ycor() + 20
        self.goto(self.xcor(), new)

    def down(self):
        new = self.ycor() - 20
        self.goto(self.xcor(), new)











