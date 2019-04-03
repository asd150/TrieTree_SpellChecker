
from tkinter import *
from tkinter import scrolledtext

app = Tk()

HEIGHT = 300
WIDTH = 400
GEOMETRY = str(WIDTH) + "x" + str(HEIGHT)

app.title("TrieTree")
app.geometry(GEOMETRY)
lable_1 = Label(app, text="Enter a word")
lable_1.grid(column = 0, row = 0)
txt_1 = Entry(app, width = 30)
txt_1.grid(column = 0, row = 1)

lable_1 = Label(app, text="Recommendation or Description")
lable_1.grid(column = 0, row = 2)

txt_2 = scrolledtext.ScrolledText(app, width = 40, height=10)
txt_2.grid(column = 0, row =3)

def clicked():
    res = txt_1.get()
    txt_2.delete(1.0, END)
    txt_2.insert(INSERT, res)

button_1 = Button(app, text = "Check Spell", command = clicked)
button_1.grid(column=1, row=1)

app.mainloop()