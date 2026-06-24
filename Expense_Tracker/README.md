# Expense Tracker

A command-line Expense Tracker built in Python.

Track your income and expenses, view your balance, and store transaction history permanently using JSON.

## Features

* Add income transactions
* Add expense transactions
* View current balance
* View transaction history
* View financial summary
* Automatic data saving
* Persistent storage using JSON
* Input validation and error handling

## Requirements

* Python 3.10+

## Run

```bash
python3 Expense_Tracker.py
```

## Menu

```text
1. Add Income
2. Add Expense
3. View Balance
4. View Transaction History
5. View Summary
6. Exit
```

## Transaction Format

Transactions are stored automatically in:

```text
history.json
```

Example:

```json
[
    {
        "type": "income",
        "amount": 5000,
        "description": "Salary"
    },
    {
        "type": "expense",
        "amount": 1200,
        "description": "Groceries"
    }
]
```

## Example Usage

```text
1. Add Income
Enter amount: 5000
Enter description: Salary

2. Add Expense
Enter amount: 1200
Enter description: Groceries

5. View Summary

Total Income= 5000.00
Total Expense= 1200.00
Current Balance= 3800.00
Total Transactions= 2
```

## Concepts Practiced

* JSON data storage
* File handling
* Functions
* Lists and dictionaries
* Input validation
* Error handling
* Program flow control
* Data persistence

## Future Improvements

* Transaction categories
* Date and time tracking
* Monthly reports
* Edit transactions
* Delete transactions
* Search functionality
* CSV export
* GUI version

## Author

Sabal
