import tkinter
window = tkinter.Tk()
window.title("this it the title of the window")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()


def button_clicked():
    text = entry.get()
    my_label.config(text=text)


button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

entry = tkinter.Entry(width=50)
entry.pack()





window.mainloop()