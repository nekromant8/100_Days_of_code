from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=280)
        self.write(f'Score: {self.score_num}', move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_num += 1
        self.clear()
        self.write(f'Score: {self.score_num}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game over.', move=False, align=ALIGNMENT, font=FONT)