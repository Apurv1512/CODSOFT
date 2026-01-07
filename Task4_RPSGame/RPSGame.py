import random
import tkinter as tk
from tkinter import messagebox

# ---------- Main Window ----------
root = tk.Tk()
root.title("CODSOFT Rock Paper Scissors Game")
root.geometry("520x580")
root.config(bg="#0f172a")

user_score = 0
computer_score = 0
tie_score = 0
choices = ["Rock", "Paper", "Scissors"]

# ---------- Title ----------
title = tk.Label(
    root,
    text="Rock ✊  Paper ✋  Scissors ✌",
    font=("Arial", 20, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title.pack(pady=10)

# ---------- Score ----------
score_label = tk.Label(
    root,
    text="Score\nYou: 0  |  Computer: 0  |  Tie: 0",
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="#a5f3fc"
)
score_label.pack(pady=10)

# ---------- Choices ----------
user_choice_label = tk.Label(
    root,
    text="Your Choice:",
    font=("Arial", 16),
    bg="#0f172a",
    fg="white"
)
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    root,
    text="Computer Choice:",
    font=("Arial", 16),
    bg="#0f172a",
    fg="white"
)
computer_choice_label.pack(pady=10)

# ---------- Result ----------
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 22, "bold"),
    bg="#0f172a",
    fg="#fde68a"
)
result_label.pack(pady=20)

thinking_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#0f172a",
    fg="#22c55e"
)
thinking_label.pack()


# ---------- GAME LOGIC ----------
def play(user_choice):
    thinking_label.config(text="Computer is thinking...")
    result_label.config(text="")
    computer_choice_label.config(text="Computer Choice: ")

    root.after(800, lambda: finish_round(user_choice))  # animation delay


def finish_round(user_choice):
    global user_score, computer_score, tie_score

    computer_choice = random.choice(choices)

    thinking_label.config(text="")
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")

    # ---------- Result Decision ----------
    if user_choice == computer_choice:
        result_label.config(text="It's a Tie", fg="#eab308")
        tie_score += 1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win", fg="#4ade80")
        user_score += 1
    else:
        result_label.config(text="You Lose", fg="#f87171")
        computer_score += 1

    # ---------- Update Score ----------
    score_label.config(
        text=f"Score\nYou: {user_score}  |  Computer: {computer_score}  |  Tie: {tie_score}"
    )

    # ---------- Auto Winner at 5 ----------
    if user_score == 5:
        messagebox.showinfo("Champion", "You Won the Match!")
        reset_game()

    elif computer_score == 5:
        messagebox.showinfo("Oops", "Computer Won the Match!")
        reset_game()


# ---------- BUTTONS ----------
frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=20)

rock_btn = tk.Button(
    frame, text="Rock ✊", width=12, height=2,
    font=("Arial", 12), command=lambda: play("Rock"),
    bg="#3b82f6", fg="white"
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    frame, text="Paper ✋", width=12, height=2,
    font=("Arial", 12), command=lambda: play("Paper"),
    bg="#22c55e", fg="white"
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    frame, text="Scissors ✌", width=12, height=2,
    font=("Arial", 12), command=lambda: play("Scissors"),
    bg="#f97316", fg="white"
)
scissors_btn.grid(row=0, column=2, padx=10)


# ---------- RESET ----------
def reset_game():
    global user_score, computer_score, tie_score
    user_score = 0
    computer_score = 0
    tie_score = 0
    score_label.config(text="Score\nYou: 0  |  Computer: 0  |  Tie: 0")
    user_choice_label.config(text="Your Choice:")
    computer_choice_label.config(text="Computer Choice:")
    result_label.config(text="")
    thinking_label.config(text="")


reset_btn = tk.Button(
    root,
    text="Reset Game",
    width=16,
    height=2,
    font=("Arial", 12),
    bg="#e11d48",
    fg="white",
    command=reset_game
)
reset_btn.pack(pady=8)


# ---------- EXIT WITH FINAL RESULT PRINT ----------
def exit_game():
    if user_score > computer_score:
        winner = "You Won the Match"
    elif computer_score > user_score:
        winner = "Computer Won the Match"
    else:
        winner = "Match Tied"

    print("\n========= Final Match Result =========")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Tie: {tie_score}")
    print(f"Winner : {winner}")
    print("=====================================\n")

    root.destroy()


exit_btn = tk.Button(
    root,
    text="Exit",
    width=16,
    height=2,
    font=("Arial", 12),
    bg="red",
    fg="white",
    command=exit_game
)
exit_btn.pack(pady=5)

root.mainloop()
