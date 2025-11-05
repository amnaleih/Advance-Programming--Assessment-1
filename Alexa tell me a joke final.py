from tkinter import *
import random

root = Tk()
root.title("Joke App")
root.geometry("350x600")

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(root)
        self.frame.pack(pady=20)

        # Load jokes from file
        with open(r"Exercise 2\randomjokes(not final).txt", encoding="utf-8") as f:
            self.jokes = [line.strip() for line in f if "?" in line]

        self.current_joke = None

        Label(self.frame, text="Type: Alexa tell me a Joke", font=("Arial", 12)).pack(pady=10)
        self.entry = Entry(self.frame, font=("Arial", 12))
        self.entry.pack(pady=5)

        Button(self.frame, text="Submit", command=self.handle_input).pack(pady=10)

        self.setup_label = Label(self.frame, text="", font=("Arial", 14), wraplength=300)
        self.setup_label.pack(pady=10)

        self.punchline_label = Label(self.frame, text="", font=("Arial", 12), wraplength=300)
        self.punchline_label.pack(pady=10)

        self.show_punch_button = Button(self.frame, text="Show Punchline", command=self.show_punchline)
        self.show_punch_button.pack(pady=5)
        self.show_punch_button.config(state=DISABLED)

        self.next_button = Button(self.frame, text="Next Joke", command=self.show_joke)
        self.next_button.pack(pady=5)
        self.next_button.config(state=DISABLED)

        Button(self.frame, text="Quit", command=root.quit).pack(pady=20)

    def handle_input(self):
        user_text = self.entry.get().strip()
        if user_text.lower() == "alexa tell me a joke":
            self.show_joke()
        else:
            self.setup_label.config(text="Say: Alexa tell me a Joke")
            self.punchline_label.config(text="")
            self.show_punch_button.config(state=DISABLED)
            self.next_button.config(state=DISABLED)

    def show_joke(self):
        self.punchline_label.config(text="")
        self.current_joke = random.choice(self.jokes)
        setup, punch = self.current_joke.split("?", 1)
        self.setup_label.config(text=setup + "?")
        self.show_punch_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)

    def show_punchline(self):
        if self.current_joke:
            setup, punch = self.current_joke.split("?", 1)
            self.punchline_label.config(text=punch.strip())
            self.show_punch_button.config(state=DISABLED)
            self.next_button.config(state=NORMAL)

app = JokeApp(root)
root.mainloop()