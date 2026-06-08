import random

MIN_LENGTH = 8
if MIN_LENGTH < 4:
    raise ValueError("MIN_LENGTH must be 4 at minimum!")

upper_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alphabets = upper_alphabets.lower()
numbers = "0123456789"
symbols = "!@#$%^&*()_-+={}[]|:;<,.>?/~"
all_characters = upper_alphabets+lower_alphabets+numbers+symbols


def create_password(length):
    password = [
        random.choice(upper_alphabets),
        random.choice(lower_alphabets),
        random.choice(numbers),
        random.choice(symbols)
    ]
    for _ in range(length-4):
        password.append(random.choice(all_characters))
    random.shuffle(password)

    final_password = "".join(password)
    return final_password


def main():
    while True:
        length = 0
        try:
            length = int(
                input(f"Enter length of password needed ( minimum {MIN_LENGTH} ):"))
            if length >= MIN_LENGTH:
                break
            print(
                f"Password needs to be atleast {MIN_LENGTH} characters long!")
        except ValueError:
            print("Enter a number!")
            pass
    while True:
        print(create_password(length))
        if input("Retry password generation? ( y to retry )") != "y":
            break


main()
