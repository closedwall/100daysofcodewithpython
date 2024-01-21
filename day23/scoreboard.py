from turtle import Turtle
FONT = ("Courier",24, "normal")
POSITION=(-220,260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_count=1
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.paint_score()
    
    def paint_score(self):
        self.write(f"Level: {self.level_count}",align="center", font=FONT)
    
    def update_score(self):
        self.clear()
        self.level_count+=1
        self.paint_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)