FONT = ("Courier",18,"normal")
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.draw_score()
    def draw_score(self):
        self.clear()
        self.penup()
        self.goto(-250,250)
        self.pendown()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.hideturtle()
    def gameover(self):
        self.clear()
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("Game Over", align="center", font = FONT)