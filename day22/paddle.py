from turtle import Turtle
# X_COR=350

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.y_pos=0
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)

    def move_up(self):
        y_cor = self.ycor() + 20
        self.y_pos = y_cor
        if self.y_pos < 250:
            self.goto(self.xcor(),self.y_pos)

    def move_down(self):
        y_cor = self.ycor() - 20
        self.y_pos = y_cor
        if self.y_pos > -250:
            self.goto(self.xcor(),self.y_pos)