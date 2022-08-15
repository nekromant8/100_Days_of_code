import random
import time
from tkinter import *
import pandas

# -------------------------------Read data-------------------------------------------------------------------
try:
    data = pandas.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    orig_data = pandas.read_csv('data/en_ru.csv')
    words = orig_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")
timer = None
current_card = {}


# -------------------------------Buttons logic---------------------------------------------------------------
def switch_card():
    canvas.itemconfig(title_text, fill='white', text=f'Russian')
    canvas.itemconfig(word_text, fill='white', text=f'{current_card["Russian"]}')
    canvas.itemconfig(canvas_image, image=new_image)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(title_text, text=f'English', fill='black')
    canvas.itemconfig(word_text, text=f'{current_card["English"]}', fill='black')
    canvas.itemconfig(canvas_image, image=image)
    flip_timer = window.after(3000, switch_card)


def is_known():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------------GUI-----------------------------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, switch_card)
# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file='images/card_front.png')
new_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=image)
title_text = canvas.create_text(400, 150, text='', fill='black', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', fill='black', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
correct_button_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_image, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()
