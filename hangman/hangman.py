import mistake_hangman
import csv
import os
import random
import sys

# 2-14=Food
# 15-27=Animals
# 28-40=Countries
# 41-53=Fictional Characters
# 54-66=Movies


def main():
    # Initialization
    mistakes = 0
    used_letters = []
    # Get random category and word
    try:
        with open("words.csv", "r") as words:
            reader = csv.DictReader(words)
            word_list = list(reader)
            random_number = random.randint(0, len(word_list) - 1)

            selected_category = word_list[random_number]["Category"]
            word_to_guess = word_list[random_number]["Word"]

            length_of_word = len(word_to_guess)
            unguessed_word = ["_"]*length_of_word

    except FileNotFoundError:
        print("words.csv file not found!")
        sys.exit()

    # Game starts
    while True:
        render_screen(mistakes, selected_category,
                      unguessed_word, used_letters)
        if mistakes == 5:
            print("Game Over!")
            break

        # Take input / validate/ update values
        used_letters, unguessed_word, mistakes = input_guess(
            word_to_guess, unguessed_word, used_letters, mistakes)

        if word_to_guess == "".join(unguessed_word):
            print("You Win!")
            break


def clear_screen():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Mac/Linux
    else:
        os.system("clear")


def render_screen(mistakes, selected_category, unguessed_word, used_letters):
    clear_screen()
    match mistakes:
        case 1:
            print(mistake_hangman.mistake_1)
        case 2:
            print(mistake_hangman.mistake_2)
        case 3:
            print(mistake_hangman.mistake_3)
        case 4:
            print(mistake_hangman.mistake_4)
        case 5:
            print(mistake_hangman.mistake_5)
        case _:
            print(mistake_hangman.mistake_0)

    print(f"Category= {selected_category}")
    print(" ".join(unguessed_word))
    print(f"Chances left: {5-mistakes}")
    print(f"Used letters: {', '.join(used_letters)}")


def input_guess(word_to_guess, unguessed_word, used_letters, mistakes):
    while True:
        guess = input().lower()
        # Check used inputs
        if guess in used_letters:
            continue
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print('INVALID GUESS (enter a-z)!')
            continue
        else:
            used_letters.append(guess)
            break

    # Update unguessed_word
    if guess in word_to_guess.lower():
        for index, letter in enumerate(word_to_guess):
            if letter.lower() == guess:
                unguessed_word[index] = letter
    else:
        mistakes += 1

    return (used_letters, unguessed_word, mistakes)


if __name__ == "__main__":
    main()
