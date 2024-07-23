import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"${len(guessed_states)}/50 Guess the name", prompt="Name the another state").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        current_state = data[data.state == answer_state]
        t.goto(current_state["x"].item(), current_state["y"].item())
        t.write(answer_state)