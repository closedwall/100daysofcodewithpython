#TODO: create hirst painting using turtle
import colorgram
import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
tim = Turtle()

#----------------------------------------------------------
#code to extract color from perticular picture
# rgb_colors=[]
# colors = colorgram.extract('hirst.jpeg', 30)

# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
#---------------------------------------------------------

color_list=[(242, 245, 249), (207, 155, 102), (57, 107, 128), (162, 82, 43), (125, 79, 97), (122, 156, 171), (126, 175, 159), (195, 142, 39), (226, 198, 130), (188, 89, 109), (191, 131, 145), (14, 44, 57), (53, 38, 19), (51, 164, 128), (59, 121, 114), (218, 90, 70), (159, 22, 32), (41, 31, 33), (8, 30, 28), (81, 146, 165), (238, 167, 162), (156, 28, 21), (23, 80, 91), (233, 168, 173), (173, 206, 188), (106, 126, 157), (26, 87, 84)]
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

tim.speed('fastest')
for dot_count in range(1,number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if(dot_count % 10) ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()

screen.exitonclick()