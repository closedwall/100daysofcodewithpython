from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()

def randomColorGenerator():
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    return (r,g,b)


# tim.shape("circle")

#TODO: 1 this section print square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


#TODO:2 code to print dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")


# TODO:3 another way to draw dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()



#TODO:4 programm to draw 4 sided shape to 10 sided shape on single base line

# def drawShape(sides):
#     angle = 360/sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.left(angle)

# for val in range(3,11):
#     color = randomColorGenerator()
#     tim.pencolor(color)
#     drawShape(val)

#TODO:5 random wal of turtle
# tim.width(8)
# tim.speed(10)
# directions = [0,90,180,270]

# for _ in range(200):
#     color = randomColorGenerator()
#     tim.pencolor(color)
#     tim.forward(20)
#     tim.setheading(random.choice(directions))


#TODO: 6 generate a spirograph
# radius = 100
# tim.speed("fastest")
# def print_spirograph(size_of_gap):
#     for _ in range(360//size_of_gap):
#         color = randomColorGenerator()
#         tim.pencolor(color)
#         tim.circle(radius, extent=None, steps=None)
#         tim.setheading(tim.heading()+size_of_gap)

# print_spirograph(1)



screen.exitonclick()
