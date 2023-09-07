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
