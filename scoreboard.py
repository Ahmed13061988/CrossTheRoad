from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230, 260)
        self.hideturtle()
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

    def passing(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)
