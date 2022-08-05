import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    check_mark_label.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    elif len(str(count_sec)) == 1:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(rep/2)
        for _ in  range(work_sessions):
            mark += '✔'
        check_mark_label.config(text=mark)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global rep

    rep += 1
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 133, text='00:00', fill='white', font=(FONT_NAME, 26, 'bold'))
canvas.grid(column=1, row=1)

#Label
timer_label = Label(font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.config(text="Timer")
timer_label.grid(column=1, row=0)

check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

#Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button =Button(text="Reset",command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)
window.mainloop()