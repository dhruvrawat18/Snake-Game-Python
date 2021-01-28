from turtle import Turtle
ALIGNMENT = "center"
FONT =("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()




