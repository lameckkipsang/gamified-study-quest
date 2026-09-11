# Gamified Study Quest 

A simple, interactive command-line interface (CLI) quiz game built in Python.

---

## Features
- **Randomized Question Order:** Uses `random.shuffle()` so questions appear in a different sequence every time you play.
- **Error Handling:** Uses ValueError so that it throws an error if and when a different choice is put that is not in line with A, B, C and D. It also uses the try except block.
- **Multiple-Choice Questions:** Clear A, B, C, and D options for every question.
- **Immediate Feedback:** Displays whether your answer is correct or incorrect along with a helpful explanation.
- **Score Tracking & Evaluation:** Calculates your final score and gives personalized feedback (**Excellent**, **Good**, or **Try Again**).

---

## Project Structure
```text
gamified-study-quest/
│
├── app.py       # Main Python script containing the quiz logic
└── README.md     # Project documentation