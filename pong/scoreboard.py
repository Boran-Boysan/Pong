from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.s1 = 0
        self.s2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.update()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.s1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.s2, align="center", font=("Courier", 80, "normal"))

    def update(self):
        self.goto(-100, 200)
        self.write(self.s1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.s2, align="center", font=("Courier", 80, "normal"))


    def increase_1(self):
        self.s1 +=1
        self.clear()
        self.update()

    def increase_2(self):
        self.s2 +=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        if self.s1 > self.s2:
            self.write(f"GAME OVER\n Player_1 wins", align="center", font=("Aria", 24, "normal"))
        else:
            self.write(f"GAME OVER\n Player_2 wins", align="center", font=("Aria", 24, "normal"))
