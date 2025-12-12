from turtle import Turtle
<<<<<<< HEAD

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
=======
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 266)

    def update_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("GAMEOVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

>>>>>>> 4c2b399dabf85833d02c07dce7674fd55e5833d1
