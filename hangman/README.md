# Hangman

A terminal-based Hangman game built in Python.

The game randomly selects a word from different categories, and the player must guess the word one letter at a time before the hangman is completely drawn.

## Features

* Random word selection
* Multiple word categories
* ASCII art hangman
* Input validation
* Tracks previously guessed letters
* Displays remaining chances
* Case-insensitive letter matching
* Terminal-based gameplay

## Categories

* Food
* Animals
* Countries
* Fictional Characters
* Movies

Words are loaded from a CSV file, making it easy to add new categories and words.

## Requirements

* Python 3.10+

No external libraries are required.

## Project Structure

```text
Hangman/
├── hangman.py
├── mistake_hangman.py
└── words.csv
```

* **hangman.py** – Main game logic
* **mistake_hangman.py** – ASCII art for each hangman stage
* **words.csv** – Word database and categories

## Run

```bash
python3 hangman.py
```

## Gameplay

1. A random category and word are selected.
2. The category is displayed.
3. Guess one letter at a time.
4. Correct guesses reveal all matching letters.
5. Incorrect guesses add a part to the hangman.
6. The game ends when:

   * The entire word is guessed, or
   * Five incorrect guesses are made.

## Example

```text
|--------
|       |
|      ***
|
|
|
|
|
|
|
|
|

Category= Animals

_ _ _ _ _ _

Chances left: 5

Used letters:
```

After a few guesses:

```text
Category= Animals

D O L _ H I N

Chances left: 2

Used letters: d, o, l, h, i, n, a, e
```

## Concepts Practiced

* File handling
* Reading CSV files
* Random selection
* Lists
* String manipulation
* Input validation
* Functions
* Modular programming
* Terminal rendering
* Control flow (`match`, loops, conditionals)

## Future Improvements

* Difficulty levels (Easy, Medium, Hard)
* Hint system
* High score tracking
* Multiplayer mode
* Save and resume games
* Colored terminal output
* Category selection by the player
* Guess the entire word option
* GUI version using Tkinter or Pygame

## Author

Sabal
