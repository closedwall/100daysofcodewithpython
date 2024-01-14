from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_start=False
# screen.bgpic('bg.png')

turtle_color =['red','yellow','indigo','green','blue']
turtles=[]
idx=0
for val in range(0,200,40):
    new_tutle = Turtle(shape="turtle")
    new_tutle.penup()
    new_tutle.goto(x=-240,y=-80+val)
    new_tutle.color(turtle_color[idx])
    turtles.append(new_tutle)
    idx+=1


bet = screen.textinput(title="make your bet",prompt="which turtle win the race? Enter the color:")

if bet:
    is_race_start=True


while is_race_start:
    for turtle in turtles:
        if turtle.xcor()>230:
            status = turtle.pencolor()
            is_race_start=False
            if(bet== status):
                print("you won the the bet! congratulations")
            else:
                print(f"You loose! the {status} won the match")
        to_move = random.randint(0,10)
        turtle.forward(to_move)


screen.exitonclick()