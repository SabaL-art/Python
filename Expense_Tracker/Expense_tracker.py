import json
import os
import sys

if os.path.exists("history.json"):
    with open("history.json", "r") as f:
        # history=transistion history
        history = json.load(f)
else:
    history = []


def calculate_balance():
    income = 0
    expense = 0
    for i in history:
        """
        JSON FILE DATA SAMPLE:
            type:(income/expense), amount, description
        """
        if i["type"] == "income":
            income += i["amount"]
        elif i["type"] == "expense":
            expense += i["amount"]
    balance = income-expense
    return income, expense, balance


def save_history():
    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)


def menu():
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance ")
        print("4. View Transaction History ")
        print("5. View Summary ")
        print("6. Exit ")
        try:
            choice = int(input("Enter choice:"))
            if choice < 1 or choice > 6:
                raise ValueError
        except ValueError:
            print("Enter number (1-6)")
            continue
        return choice


def add_income():
    while True:
        print("\n---Add Income---")
        try:
            new_income = int(input("Enter amount:"))
        except ValueError:
            print("Enter amount in integer!")
            continue
        break
    description = input("Enter description:")

    history.append({
        "type": "income",
        "amount": new_income,
        "description": description
    })


def main():
    income, expense, balance = calculate_balance()
    while True:
        choice = menu()
        match choice:
            case 1:
                add_income()
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 5:
                ...
            case 6:
                save_history()
                sys.exit()


if "__name__" == "__main__":
    main()
