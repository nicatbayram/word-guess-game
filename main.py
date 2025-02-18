import tkinter as tk
from tkinter import ttk, messagebox
import random
from typing import Set, List
import json
import os

class WordGuessingGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Word Guessing Game")
        self.root.geometry("800x500")
        
        # Game state
        self.words = ["PYTHON", "PROGRAMMING", "COMPUTER", "ALGORITHM", "DATABASE"]
        self.current_word = ""
        self.guessed_letters: Set[str] = set()
        self.max_tries = 6
        self.remaining_tries = self.max_tries
        self.game_active = False
        self.scores = self.load_scores()
        
        # Styling
        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=('Helvetica', 10))
        self.style.configure("Title.TLabel", font=('Helvetica', 24, 'bold'))
        self.style.configure("Word.TLabel", font=('Helvetica', 18))
        self.style.configure("Score.TLabel", font=('Helvetica', 12))
        
        # Create frames
        self.menu_frame = ttk.Frame(self.root, padding="20")
        self.game_frame = ttk.Frame(self.root, padding="20")
        self.rules_frame = ttk.Frame(self.root, padding="20")
        
        self.setup_menu()
        self.setup_game()
        self.setup_rules()
        self.show_menu()

    def setup_menu(self):
        # Title
        title = ttk.Label(self.menu_frame, text="Word Guessing Game", style="Title.TLabel")
        title.pack(pady=20)
        
        # Buttons
        ttk.Button(self.menu_frame, text="Start Game", command=self.start_game).pack(pady=10)
        ttk.Button(self.menu_frame, text="Rules", command=self.show_rules).pack(pady=10)
        
        # High Scores
        self.scores_frame = ttk.Frame(self.menu_frame)
        self.scores_frame.pack(pady=20)
        self.update_scores_display()

    def setup_game(self):
        # Word display
        self.word_display = ttk.Label(self.game_frame, text="", style="Word.TLabel")
        self.word_display.pack(pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.game_frame, length=200, mode='determinate')
        self.progress.pack(pady=10)
        
        # Hint label
        self.hint_label = ttk.Label(self.game_frame, text="")
        self.hint_label.pack(pady=10)
        
        # Keyboard frame
        keyboard_frame = ttk.Frame(self.game_frame)
        keyboard_frame.pack(pady=20)
        
        # Create keyboard buttons
        self.letter_buttons = {}
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, letter in enumerate(letters):
            row = i // 9
            col = i % 9
            btn = ttk.Button(keyboard_frame, text=letter, width=3,
                           command=lambda l=letter: self.handle_guess(l))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.letter_buttons[letter] = btn
        
        # Back to menu button
        ttk.Button(self.game_frame, text="Back to Menu", 
                  command=self.return_to_menu).pack(pady=20)

    def setup_rules(self):
        # Rules text
        title = ttk.Label(self.rules_frame, text="How to Play", style="Title.TLabel")
        title.pack(pady=20)
        
        rules_text = """
        1. Try to guess the hidden word one letter at a time
        2. You have 6 attempts to guess incorrectly before losing
        3. A hint will be shown after 3 wrong guesses
        4. The progress bar shows your remaining attempts
        5. Your scores will be saved for completed games
        """
        
        rules_label = ttk.Label(self.rules_frame, text=rules_text, justify="left")
        rules_label.pack(pady=20)
        
        # Back button
        ttk.Button(self.rules_frame, text="Back to Menu",
                  command=self.show_menu).pack(pady=10)

    def start_game(self):
        self.current_word = random.choice(self.words)
        self.guessed_letters = set()
        self.remaining_tries = self.max_tries
        self.game_active = True
        self.hint_label.config(text="")
        
        # Reset keyboard buttons
        for btn in self.letter_buttons.values():
            btn.config(state="normal")
        
        self.update_display()
        self.show_game()

    def handle_guess(self, letter: str):
        if not self.game_active:
            return
        
        self.guessed_letters.add(letter)
        self.letter_buttons[letter].config(state="disabled")
        
        if letter not in self.current_word:
            self.remaining_tries -= 1
            
            # Show hint after 3 wrong guesses
            if self.remaining_tries == self.max_tries - 3:
                self.hint_label.config(
                    text=f"Hint: The word is {len(self.current_word)} letters long")
        
        self.update_display()
        self.check_game_end()

    def update_display(self):
        # Update word display
        display_word = ""
        for letter in self.current_word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        self.word_display.config(text=display_word)
        
        # Update progress bar
        progress = (self.remaining_tries / self.max_tries) * 100
        self.progress['value'] = progress

    def check_game_end(self):
        word_completed = all(letter in self.guessed_letters 
                           for letter in self.current_word)
        
        if word_completed:
            self.game_active = False
            self.save_score()
            messagebox.showinfo("Congratulations!", 
                              f"You won! The word was {self.current_word}")
            self.return_to_menu()
        elif self.remaining_tries <= 0:
            self.game_active = False
            messagebox.showinfo("Game Over", 
                              f"You lost! The word was {self.current_word}")
            self.return_to_menu()

    def save_score(self):
        score = {
            'word': self.current_word,
            'tries_remaining': self.remaining_tries
        }
        self.scores.append(score)
        self.scores = sorted(self.scores, 
                           key=lambda x: x['tries_remaining'], 
                           reverse=True)[:5]  # Keep top 5 scores
        
        with open('scores.json', 'w') as f:
            json.dump(self.scores, f)

    def load_scores(self) -> List[dict]:
        try:
            with open('scores.json', 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def update_scores_display(self):
        for widget in self.scores_frame.winfo_children():
            widget.destroy()
        
        if self.scores:
            ttk.Label(self.scores_frame, 
                     text="High Scores", 
                     style="Score.TLabel").pack()
            
            for score in self.scores:
                score_text = f"{score['word']} - {score['tries_remaining']} tries left"
                ttk.Label(self.scores_frame, 
                         text=score_text, 
                         style="Score.TLabel").pack()

    def show_menu(self):
        self.game_frame.pack_forget()
        self.rules_frame.pack_forget()
        self.menu_frame.pack()
        self.update_scores_display()

    def show_game(self):
        self.menu_frame.pack_forget()
        self.rules_frame.pack_forget()
        self.game_frame.pack()

    def show_rules(self):
        self.menu_frame.pack_forget()
        self.game_frame.pack_forget()
        self.rules_frame.pack()

    def return_to_menu(self):
        self.game_active = False
        self.show_menu()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = WordGuessingGame()
    game.run()