from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self. coordinates = coordinates
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(self.coordinates)

    def go_up(self):
        new_ypos = self.ycor() + 30
        self.goto(self.xcor(), y=new_ypos)

    def go_down(self):
        new_ypos = self.ycor() - 30
        self.goto(self.xcor(), y=new_ypos)
