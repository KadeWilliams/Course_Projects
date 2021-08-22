from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = quiz_brain.score
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text=f"Score: {self.score}", padx=20, pady=20, font=('Arial', 15, 'normal'), bg=THEME_COLOR,
                                fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text='question', font=('Arial', 20, 'italic'),
                                                     fill='black', width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, bg=THEME_COLOR,
                                  relief='flat', activebackground=THEME_COLOR, command=self.true)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, bg=THEME_COLOR,
                                   relief='flat', activebackground=THEME_COLOR, command=self.false)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true(self):
        self.give_feedback(self.quiz.check_answer('True'))


    def false(self):
        self.give_feedback(self.quiz.check_answer('False'))


    def give_feedback(self, answer: bool):
        self.score = self.quiz.score
        self.score_label.config(text=f"Score: {self.score}")
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


