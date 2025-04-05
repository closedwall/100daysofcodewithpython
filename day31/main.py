import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_choice = {}
to_learn = {}

try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient='records')


def next_card():
    global current_choice, flip_timer
    window.after_cancel(flip_timer)
    current_choice = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_choice['French'], fill="black")
    canvas.itemconfig(card_img_id, image=card_font_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_choice['English'], fill="white")
    canvas.itemconfig(card_img_id, image=card_back_img)


def is_known():
    to_learn.remove(current_choice)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_font_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img_id = canvas.create_image(400, 263, image=card_font_img)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()


window.mainloop()
