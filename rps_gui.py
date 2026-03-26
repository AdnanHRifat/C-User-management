from tkinter import Tk, Canvas, Frame, Label, Button
from PIL import Image, ImageTk
import random
#Gui design
class RPSFullControlGUI:
    def __init__(self, root, bg_path):
        self.root = root
        self.root.title("Rock Paper Scissors - Game Edition")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # self.bg_image = Image.open(bg_path).resize((800, 600))
        # self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = Canvas(self.root, width=800, height=600, bg="lightblue")
        self.canvas.pack(fill="both", expand=True)
        # self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.choices = ["rock", "paper", "scissors"]
        self.emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

        self.choice_buttons = []
        self.result_frame = None

        self.setup_ui()
        self.reset_game()

    def setup_ui(self):
        self.canvas.create_text(400, 50, text="🎮 ROCK  PAPER  SCISSORS 🎮", font=("Impact", 30, "bold"),
                                fill="white", anchor="center")

        self.status_label = Label(self.root, text="", font=("Arial", 14, "bold"),
                                  bg="#ffffff", fg="#2c3e50")
        self.canvas.create_window(400, 100, window=self.status_label)

        self.user_label = Label(self.root, text="You: ❔", font=("Arial", 36, "bold"), bg="#ffffff")
        self.computer_label = Label(self.root, text="Computer: ❔", font=("Arial", 36, "bold"), bg="#ffffff")

        self.canvas.create_window(220, 180, window=self.user_label)
        self.canvas.create_text(400, 180, text="VS", font=("Arial", 20, "bold"), fill="white")
        self.canvas.create_window(580, 180, window=self.computer_label)

        self.button_frame = Frame(self.root, bg="#ffffff")
        self.canvas.create_window(400, 270, window=self.button_frame)

        for choice in self.choices:
            btn = Button(
                self.button_frame,
                text=f"{self.emojis[choice]} {choice.title()}",
                font=("Arial", 12, "bold"),
                bg="#2980b9",
                fg="white",
                activebackground="#3498db",
                padx=10,
                pady=5,
                relief="raised",
                bd=3,
                command=lambda c=choice: self.play(c)
            )
            btn.pack(side="left", padx=10)
            self.choice_buttons.append(btn)

        self.score_label = Label(self.root, text="", font=("Arial", 12, "bold"),
                                 bg="#ffffff", fg="#2c3e50")
        self.canvas.create_window(400, 330, window=self.score_label)

        self.control_frame = Frame(self.root, bg="#ffffff")
        self.canvas.create_window(400, 390, window=self.control_frame)

        self.play_again_btn = Button(self.control_frame, text="🔁 Reset", font=("Arial", 11, "bold"),
                                     bg="#2ecc71", fg="white", command=self.reset_game)
        self.play_again_btn.pack(side="left", padx=15)

        self.quit_btn = Button(self.control_frame, text="❌ Quit", font=("Arial", 11, "bold"),
                               bg="#e74c3c", fg="white", command=self.root.quit)
        self.quit_btn.pack(side="left", padx=15)

    def reset_game(self):
        self.round = 1
        self.score = {"Wins": 0, "Losses": 0, "Ties": 0}
        self.user_label.config(text="You: ❔")
        self.computer_label.config(text="Computer: ❔")
        self.status_label.config(text="Choose your move!", fg="#2c3e50")
        self.score_label.config(text=self.format_score())
        for btn in self.choice_buttons:
            btn.config(state="normal")
        if self.result_frame:
            self.result_frame.destroy()

    def format_score(self):
        return f"Round: {self.round}   Wins: {self.score['Wins']}   Losses: {self.score['Losses']}   Ties: {self.score['Ties']}"

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)

        self.user_label.config(text=f"You: {self.emojis[player_choice]}")
        self.computer_label.config(text=f"Computer: {self.emojis[computer_choice]}")

        result = self.get_result(player_choice, computer_choice)

        if result == "win":
            self.status_label.config(text="You win this round! 🎉", fg="#27ae60")
            self.score["Wins"] += 1
        elif result == "lose":
            self.status_label.config(text="Computer wins! 😢", fg="#c0392b")
            self.score["Losses"] += 1
        else:
            self.status_label.config(text="It's a tie! 😐", fg="#2980b9")
            self.score["Ties"] += 1

        self.round += 1
        self.score_label.config(text=self.format_score())

    def get_result(self, player, computer):
        if player == computer:
            return "tie"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "win"
        else:
            return "lose"

# Run the app
image_path = r"C:\Users\HP\Downloads\Basic coding\370e5c43-7476-45a6-a344-9210dfbace0f.png"
root = Tk()
app = RPSFullControlGUI(root, image_path)
root.mainloop()
