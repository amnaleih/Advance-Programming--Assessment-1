from tkinter import *
import random   # <-- you need this for randint and choice

root = Tk()
root.title("Math Quiz")
root.geometry("350x600")

# -----------------------------
# Simple Arithmetic Quiz App
# -----------------------------

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

        # Main frame to hold widgets
        self.frame = Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.show_menu()

    # Show difficulty menu
    def show_menu(self):
        self.clear_frame()
        Label(self.frame, text="DIFFICULTY LEVEL", font=("Arial", 16)).pack(pady=10)
        Button(self.frame, text="1. Easy", width=20, command=lambda: self.start_quiz(1)).pack(pady=5)
        Button(self.frame, text="2. Moderate", width=20, command=lambda: self.start_quiz(2)).pack(pady=5)
        Button(self.frame, text="3. Advanced", width=20, command=lambda: self.start_quiz(3)).pack(pady=5)

    # Generate random numbers based on difficulty
    def randomInt(self, level):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        else:
            return random.randint(1000, 9999)

    # Randomly choose + or -
    def decideOperation(self):
        return random.choice(['+', '-'])

    # Start quiz
    def start_quiz(self, level):
        self.level = level
        self.score = 0
        self.question_num = 0
        self.next_question()

    # Show next question
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

        Label(self.frame, text=f"Question {self.question_num}/10", font=("Arial", 14)).pack(pady=10)
        self.problem_label = Label(self.frame, text=f"{self.num1} {self.op} {self.num2} = ?", font=("Arial", 18))
        self.problem_label.pack(pady=10)

        self.answer_entry = Entry(self.frame, font=("Arial", 14))
        self.answer_entry.pack(pady=5)
        self.answer_entry.focus()

        Button(self.frame, text="Submit", command=self.check_answer).pack(pady=10)
        self.feedback_label = Label(self.frame, text="", font=("Arial", 12))
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
                self.feedback_label.config(text="Correct on second try! +5 points")
            self.root.after(1000, self.next_question)
        else:
            if self.attempt == 1:
                self.feedback_label.config(text="Incorrect. Try again.")
                self.attempt += 1
                self.answer_entry.delete(0, END)
            else:
                self.feedback_label.config(text=f"Wrong again! Answer was {correct_ans}.")
                self.root.after(1500, self.next_question)

    # Show results
    def display_results(self):
        self.clear_frame()
        Label(self.frame, text="QUIZ COMPLETE!", font=("Arial", 16)).pack(pady=10)
        Label(self.frame, text=f"Your final score: {self.score}/100", font=("Arial", 14)).pack(pady=5)

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

        Label(self.frame, text=f"Your grade: {grade}", font=("Arial", 14)).pack(pady=5)

        Button(self.frame, text="Play Again", command=self.show_menu).pack(pady=10)
        Button(self.frame, text="Exit", command=self.root.quit).pack(pady=5)

    # Clear frame
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

# -----------------------------
# Run the app
# -----------------------------
app = QuizApp(root)
root.mainloop()
