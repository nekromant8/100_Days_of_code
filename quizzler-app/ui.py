THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brane: QuizBrain):
        self.quiz = quiz_brane
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=256, bg='old lace', highlightthickness=0)
        self.c_text = self.canvas.create_text(150, 128, width=280, text='Some text', fill='grey26',
                                              font=('Source Sans Pro', 16, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score = Label(font=('Arial', 10), fg='white', bg=THEME_COLOR)
        self.score.config(text="Score: 0")
        self.score.grid(column=1, row=0)
        true_button_image = PhotoImage(file="images/true.png")
        false_button_image = PhotoImage(file="images/false.png")
        self.true = Button(image=true_button_image, highlightthickness=0, command=self.right)
        self.true.grid(column=0, row=2)
        self.false = Button(image=false_button_image, highlightthickness=0, command=self.wrong)
        self.false.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='old lace')
        if self.quiz.still_has_questions():

            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.c_text, text=q_text)
        else:
            self.canvas.itemconfig(self.c_text, text="You've reached end of the questions...")
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def right(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='sea green')
        else:
            self.canvas.config(bg='firebrick1')
        self.window.after(1000, self.get_next_question)


