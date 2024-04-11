from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highScore.txt") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highScore.txt", mode="w") as highScoreFile:
                highScoreFile.write(f"{self.highScore}")
        self.score = 0
        self.updateScoreboard()

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()