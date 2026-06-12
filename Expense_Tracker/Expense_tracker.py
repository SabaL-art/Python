import json
import os
import sys

if os.path.exists("history.json"):
    try:
        with open("history.json", "r") as f:
            # history=transistion history
            history = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        history = []
else:
    history = []


def calculate_balance():
    income = 0
    expense = 0
    """
    JSON FILE DATA SAMPLE:
        type:(income/expense), amount, description
    """
    for transaction in history:
        if transaction["type"] == "income":
            income += transaction["amount"]
        elif transaction["type"] == "expense":
            expense += transaction["amount"]
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
            new_income = float(input("Enter amount:"))
            if new_income <= 0:
                print("Enter a positive number!")
                continue
        except ValueError:
            print("Enter valid number!")
            continue
        break
    description = input("Enter description:")

    history.append({
        "type": "income",
        "amount": new_income,
        "description": description
    })
    save_history()


def add_expense():
    while True:
        print("\n---Add Expense---")
        try:
            new_expense = float(input("Enter amount:"))
            if new_expense <= 0:
                print("Enter a positive number!")
                continue
        except ValueError:
            print("Enter valid number!")
            continue
        break
    description = input("Enter description:")

    history.append({
        "type": "expense",
        "amount": new_expense,
        "description": description
    })
    save_history()


def show_balance():
    income, expense, balance = calculate_balance()
    print("---Balance---")
    print(f"Balance= {balance:.2f}")
    input("Press ENTER key to go back")


def show_history():
    print("---Transaction History---")
    if not history:
        print("No transaction history!")
    else:
        for i, transaction in enumerate(history, start=1):
            print(
                f"{i} [{transaction['type'].upper()}] {transaction['amount']:.2f} - {transaction['description']}"
            )
    input("Press ENTER key to go back")


def show_summary():
    income, expense, balance = calculate_balance()
    print("---Summary---")
    print(f"Total Income= {income:.2f}")
    print(f"Total Expense= {expense:.2f}")
    print(f"Current Balance=  {balance:.2f}")
    print(f"Total Transactions= {len(history)}")
    input("Press ENTER key to go back")


def main():
    while True:
        choice = menu()
        match choice:
            case 1:
                add_income()
            case 2:
                add_expense()
            case 3:
                show_balance()
            case 4:
                show_history()
            case 5:
                show_summary()
            case 6:
                sys.exit()
            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    main()
