from tkinter import *
import random   # for radint and choice

root = Tk()
root.title("Math Quiz")
root.geometry("350x600")

# Math Quiz Application
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.question_num = 0
        self.level = None
        self.num1 = 0
        self.num2 = 0
        self.op = "+"
        self.attempt = 1
        
        # Main frame to hold the widgets
        self.frame = Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.show_menu()

    # Show the difficulty menu
    def show_menu(self):
        self.clear_frame()
        Label(self.frame, text="DIFFICULTY LEVEL", font=("Georgia", 16)).pack(pady=10)
        Button(self.frame, text="1. Easy", width=20, command=lambda: self.start_quiz(1)).pack(pady=5)
        Button(self.frame, text="2. Moderate", width=20, command=lambda: self.start_quiz(2)).pack(pady=5)
        Button(self.frame, text="3. Advanced", width=20, command=lambda: self.start_quiz(3)).pack(pady=5)

    # Generating random numbers based on the difficulty of the quiz 
    def randomInt(self, level):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        else:
            return random.randint(1000, 9999)

    # Randomly choose whether it is addition or minus
    def decideOperation(self):
        return random.choice(['+', '-'])

    # Start of the quiz
    def start_quiz(self, level):
        self.level = level
        self.score = 0
        self.question_num = 0
        self.next_question()

    # Show the next questions
    def next_question(self):
        if self.question_num == 10:
            self.display_results()
            return

        self.clear_frame()
        self.question_num += 1
        self.attempt = 1
        self.num1 = self.randomInt(self.level)
        self.num2 = self.randomInt(self.level)
        self.op = self.decideOperation()

        Label(self.frame, text=f"Question {self.question_num}/10", font=("Georgia", 14)).pack(pady=10)
        self.problem_label = Label(self.frame, text=f"{self.num1} {self.op} {self.num2} = ?", font=("Georgia", 18))
        self.problem_label.pack(pady=10)

        self.answer_entry = Entry(self.frame, font=("Georgia", 14))
        self.answer_entry.pack(pady=5)
        self.answer_entry.focus()

        Button(self.frame, text="Submit", command=self.check_answer).pack(pady=10)
        self.feedback_label = Label(self.frame, text="", font=("Georgia", 12))
        self.feedback_label.pack(pady=5)

    # Check answer
    def check_answer(self):
        try:
            user_ans = int(self.answer_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a number.")
            return

        correct_ans = self.num1 + self.num2 if self.op == '+' else self.num1 - self.num2

        if user_ans == correct_ans:
            if self.attempt == 1:
                self.score += 10
                self.feedback_label.config(text="Correct! +10 points")
            else:
                self.score += 5
                self.feedback_label.config(text="Correct on your second try! You have gained +5 points!")
            self.root.after(1000, self.next_question)
        else:
            if self.attempt == 1:
                self.feedback_label.config(text="Incorrect. Please try again.")
                self.attempt += 1
                self.answer_entry.delete(0, END)
            else:
                self.feedback_label.config(text=f"Wrong again! The answer was {correct_ans}.")
                self.root.after(1500, self.next_question)

    # Shows the results
    def display_results(self):
        self.clear_frame()
        Label(self.frame, text="QUIZ COMPLETE!", font=("Georgia", 16)).pack(pady=10)
        Label(self.frame, text=f"Your final score for this quiz: {self.score}/100", font=("Arial", 14)).pack(pady=5)

        if self.score >= 90:
            grade = "A+"
        elif self.score >= 80:
            grade = "A"
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        elif self.score >= 50:
            grade = "D"
        else:
            grade = "F"

        Label(self.frame, text=f"Your grade: {grade}", font=("Georgia", 14)).pack(pady=5)

        Button(root, text="Play Again", command=self.show_menu).pack(pady=10)
        Button(root.frame, text="Exit", command=self.root.quit).pack(pady=5)

    # Clears frame
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# Runs the app
app = QuizApp(root)
root.mainloop()
