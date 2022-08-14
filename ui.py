from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg= THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas()
        self.canvas.configure(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Bruh ", font=("Arial 18 italic"), fill="#375362", width=280)
        self.canvas.grid(columnspan=2, row=1, column=0)


        self.checkbutton = Button()
        check_mark = PhotoImage(file = 'images/true.png')
        self.checkbutton.configure(image=check_mark, command=self.answerfalse)
        self.checkbutton.grid(row=2, column =0, pady=30)

        self.xbutton = Button()
        x_mark = PhotoImage(file='images/false.png')
        self.xbutton.configure(image=x_mark, command=self.answertrue)
        self.xbutton.grid(row=2, column=1, pady=30)

        self.label = Label()
        self.label.configure(text="score:", bg=THEME_COLOR, fg="#F8F8FF", font= ("TimesNewRoman 16"))
        self.label.grid(column=1, row=0, pady=30)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():


            self.label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.xbutton.config(state="disabled")
            self.checkbutton.config(state="disabled")
    def answertrue(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def answerfalse(self):
        self.give_feedback(self.quiz.check_answer("false"))


    def give_feedback(self, is_right):
        is_right = is_right
        if is_right:
            self.canvas.configure(bg= "green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)