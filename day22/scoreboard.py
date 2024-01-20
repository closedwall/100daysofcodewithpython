from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.l_score=0
        self.r_score=0
        self.hideturtle()
        self.update_scoreboard()
    
    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"Score: {self.l_score}", align="center", font=("Arial",15,'normal'))
        self.goto(100, 270)
        self.write(f"Score: {self.r_score}", align="center", font=("Arial",15,'normal'))
