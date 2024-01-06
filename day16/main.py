from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('circle')
timmy.color("red")
timmy.begin_fill()
while True:
    timmy.forward(100)
    timmy.left(120)
    timmy.forward(100)
    if abs(timmy.pos()) < 1:
        break
timmy.end_fill()

my_screen = Screen()
my_screen.exitonclick()

