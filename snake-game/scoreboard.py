from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg = "Game Over", align = "center", font = ("Arial", 16, "normal"))