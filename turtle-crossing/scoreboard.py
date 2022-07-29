from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_num = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(x=-290, y=260)
        self.write(f'Level: {self.level_num}', move=False, font=FONT)

    def increase_score(self):
        self.level_num += 1
        self.clear()
        self.write(f'Level: {self.level_num}', move=False, font=FONT)

    def game_over(self):
        self.home()
        self.write(f'Game over.', move=False, align='center',  font=FONT)
