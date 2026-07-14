# Password Generator

A terminal-based Password Generator built in Python.

Generate strong random passwords of any length while ensuring every password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.

## Features

- Secure random password generation
- User-defined password length
- Enforces a minimum password length
- Guarantees at least:
  - One uppercase letter
  - One lowercase letter
  - One number
  - One symbol
- Randomly shuffles characters for better randomness
- Generate unlimited passwords in one session

## Requirements

- Python 3.10+

## Run

```bash
python3 generate_password.py
```

## Usage

1. Enter the desired password length.
2. The minimum allowed length is **8** characters.
3. A strong random password is generated.
4. Choose whether to generate another password.

Example:

```text
Enter length of password needed ( minimum 8 ):12

Y!4gq@Pm8$Lz

Retry password generation? ( y to retry )
```

## Password Rules

Every generated password contains:

- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

The remaining characters are selected randomly from all available character types.

## Character Set

| Type | Characters |
|------|------------|
| Uppercase | A-Z |
| Lowercase | a-z |
| Numbers | 0-9 |
| Symbols | `!@#$%^&*()_-+={}[]\|:;<,.>?/~` |

## Concepts Practiced

- Functions
- Lists
- Random module
- String manipulation
- Input validation
- Loops
- Exception handling
- Character shuffling

## Future Improvements

- Copy password directly to clipboard
- Exclude ambiguous characters (O, 0, l, I)
- Custom character set selection
- Password strength indicator
- Save generated passwords
- GUI version using Tkinter
- Cryptographically secure generation using Python's `secrets` module

## Author

Sabal