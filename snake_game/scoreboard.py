from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.high_score = int(self.check_high_score())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=280)
        self.write(f'Score: {self.score_num} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score_num} High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def check_high_score(self):
        with open('data.txt', "r") as f:
            data = f.read()
            return data

    def update_high_score(self):
        with open('data.txt', "w") as f:
            f.write(str(self.score_num))

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            self.update_high_score()
        self.score_num = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score_num += 1
        self.update_scoreboard()
