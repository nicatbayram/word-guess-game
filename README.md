# Word Guessing Game

## Overview
The **Word Guessing Game** is a simple yet engaging game developed using Python's Tkinter library. Players attempt to guess a hidden word one letter at a time, with a limited number of incorrect guesses before losing the game. The game includes a graphical user interface with a virtual keyboard, progress bar, and high score tracking.

## Features
- **Graphical User Interface (GUI):** Built with Tkinter for a smooth and interactive experience.
- **Virtual Keyboard:** Allows players to click letters to make guesses.
- **Word Guessing Mechanism:** Players guess letters until they reveal the full word.
- **Limited Attempts:** Players have six incorrect attempts before the game ends.
- **Hints:** A hint is displayed after three incorrect guesses.
- **Progress Bar:** Displays remaining attempts.
- **High Scores:** Stores the top 5 scores in a JSON file.
- **Rules Screen:** A separate screen displaying game instructions.

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.x recommended).
You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository
```sh
git clone https://github.com/nicatbayram/word-guess-game.git
cd word-guessing-game
```

### Install Dependencies
No additional dependencies are required beyond the built-in Tkinter module.

## Usage
To start the game, run the following command:
```sh
python main.py
```

## How to Play
1. Click **Start Game** to begin.
2. A hidden word is displayed with underscores (_).
3. Click letters on the virtual keyboard to guess.
4. If the letter is correct, it appears in the word.
5. If the letter is incorrect, your remaining attempts decrease.
6. After 3 incorrect guesses, a hint appears.
7. The game ends when you guess the full word or run out of attempts.
8. Scores are saved, and the top 5 are displayed in the menu.

## File Structure
```
word-guessing-game/
│── main.py           # Main game script
│── scores.json       # Stores high scores
│── README.md         # Documentation
```

## Future Improvements
- Add more words dynamically.
- Implement difficulty levels.
- Improve UI/UX design.

## ScreenShots
<img width="400" alt="111" src="https://github.com/user-attachments/assets/e047649f-2493-4583-9804-8daea0b70452" />
<img width="400" alt="222" src="https://github.com/user-attachments/assets/1a53c012-5f3a-4185-a3a5-6d10fef92eff" />








