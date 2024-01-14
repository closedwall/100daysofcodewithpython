from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.setheading(0)
    tim.forward(100)

def move_backward():
    tim.setheading(180)
    tim.forward(100)

def move_up():
    tim.setheading(90)
    tim.forward(100)

def move_down():
    tim.setheading(-90)
    tim.forward(100)
    tim.circle(40)


screen.listen()

screen.onkey(key='Right', fun=move_forward)
screen.onkey(key='Left', fun=move_backward)
screen.onkey(key='Up', fun=move_up)
screen.onkey(key='Down', fun=move_down)

screen.exitonclick()