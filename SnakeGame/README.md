# Snake Game

A terminal-based Snake game built in Python.

Control the snake using **W, A, S, D** keys, eat apples to grow longer, and try to beat your highest score without crashing into walls or yourself.

## Features

- Real-time keyboard input
- Snake growth mechanics
- Apple spawning system
- Collision detection
- High score saving
- Score tracking
- Terminal-based gameplay
- Cross-platform screen clearing (Windows/Linux)

## Requirements

- Python 3.10+
- pynput

## Installation

Install the required dependency:

```bash
pip install pynput
```

## Run

```bash
python3 snake.py
```

## Controls

| Key | Action |
|------|----------|
| W | Move Up |
| A | Move Left |
| S | Move Down |
| D | Move Right |

## Gameplay

- The snake starts with a length of 1.
- Eat apples (`A`) to increase your score and grow longer.
- Avoid hitting:
  - Walls
  - Your own body
- The game ends when a collision occurs.

## Symbols

| Symbol | Meaning |
|----------|----------|
| @ | Snake Head |
| O | Snake Body |
| A | Apple |
| # | Border |

## High Score

The highest score is automatically saved in:

```text
high_score.txt
```

and loaded again when the game is restarted.

## Example

```text
Score= 5
High Score= 12

##########################################
#                                        #
#        OOO@                            #
#                                        #
#                    A                   #
#                                        #
##########################################
```

## Concepts Practiced

- Object-Oriented Programming (OOP)
- Game loops
- Keyboard event handling
- File handling
- Collision detection
- Lists and data structures
- Terminal rendering

## Future Improvements

- Pause functionality
- Adjustable difficulty levels
- Colored terminal graphics
- Sound effects
- Multiple apples
- Obstacles
- Better snake graphics
- GUI version using Pygame

## Author

Sabal