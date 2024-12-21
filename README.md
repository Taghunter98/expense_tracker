# Expense Tracker

A simple command-line Python application for tracking payments and expenses. This tool allows users to add, display, and delete payments, as well as view expenses by month.

## Features

- Add a new payment with description and amount.
- Display all payments with details (description, amount, date, and ID).
- Delete a payment by its unique ID.
- Find payments made in a specific month and calculate the total expenditure for that month.

## Requirements

- Python 3.x
- No external libraries required (built-in Python libraries used).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Taghunter98/expense_tracker.git
   ```

2. Navigate into the project directory:

   ```bash
   cd expense_tracker
   ```

3. Run the application:

   ```bash
   python expense_tracker.py
   ```

## Usage

### Add a Payment

Add a new payment with a description and amount.

```bash
python expense_tracker.py -a "Starbucks" 15.50
```

### Display All Payments

Display all saved payments.

```bash
python expense_tracker.py -d
```

### Delete a Payment

Delete a payment by its unique ID.

```bash
python expense_tracker.py -rm 2
```

### Find Payments by Month

Find payments made in a specific month (use the month number, e.g., `1` for January, `11` for November).

```bash
python expense_tracker.py -f 11
```

This will display all payments made in November and calculate the total expenditure for that month.

## Classes and Methods

### Payment Class

- **`__init__(self, description, amount)`**: Constructor to create a new Payment object.
- **`to_dict(self)`**: Converts the Payment object to a dictionary for JSON serialization.
- **`from_dict(cls, data)`**: Class method to create a Payment object from a dictionary.

### Payment Management

- **`generate_unique_id()`**: Generates and returns a unique payment ID by reading and updating `idtracker.txt`.
- **`load_payments()`**: Loads payment data from `payments.json` into a list of `Payment` objects.
- **`save_to_json(payment)`**: Saves a new Payment object to `payments.json`.
- **`parse_json()`**: Reads and returns the list of payments from `payments.json`.
- **`display_payment(payment, index)`**: Displays a single payment's details.
- **`display_payments()`**: Displays all saved payments.
- **`delete_payment(id)`**: Deletes a payment with a given ID.
- **`find_month(find_month)`**: Finds and displays payments made in a specific month and calculates the total expenditure.

### ExpenseTracker Class

- **`__init__(self)`**: Initialises the expense tracker and sets up command-line arguments.
- **`setup_parser(self)`**: Configures the argument parser for various commands.
- **`run(self)`**: Runs the program based on user input (add, display, remove, or find payments).
- **`add_payment(self, description, amount)`**: Adds a new payment.
- **`display_payments(self)`**: Displays all payments.

## File Structure

```
expense_tracker/
│
├── expense_tracker.py         # Main program file
├── payments.json              # Stores payment data in JSON format
├── idtracker.txt              # Stores the last used payment ID
└── README.md                  # Project documentation
```

## Contributing

Feel free to open issues or submit pull requests for improvements, bug fixes, or new features!

---
