from datetime import date
import json
import os
import random

class Payment:
    # setup class
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.date = str(date.today())
        self.id = generate_unique_id()

    # Dictate to JSON
    def to_dict(self):
        return {"description": self.description, "amount": self.amount, "date": self.date}
    
    @classmethod
    def from_dict(cls, data):
        payment = cls(data["description"], data["amount"])
        payment.date = data["date"]
        return payment
    

ID_FILE = "idtracker.txt"
def generate_unique_id():
    # Check for file
    if not os.path.exists(ID_FILE):
        with open(ID_FILE, "w") as file:
            file.write("1")
        return 1
    
    with open(ID_FILE, "r") as file:
        last_id = int(file.read().strip())
    
    new_id = last_id + 1
    
    with open(ID_FILE, "w") as file:
        file.write(str(new_id))
    
    return new_id

FILE = "payments.json"

# JSON handling
def load_payments():
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
            return [Payment.from_dict(item) for item in data]
    except FileNotFoundError:
        return []

def save_to_json(payment):
    # Load data from JSON
    try:
        if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
            with open(FILE, "r") as file:
                data = json.load(file) 
        else:
            data = []
    except (json.JSONDecodeError, FileNotFoundError):
        data = []  # Handle invalid JSON or missing file

    # Add the new payment
    data.append({"description": payment.description, "amount": payment.amount, "date": payment.date, "id": payment.id})

    # Write back to the JSON file
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)



# Payments logic
payments = []

def new_payment(description, amount):
    if not description.strip():
        print("Error: Description cannot be empty.")
        return
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Error: Amount must be a positive number.")
        return

    payment = Payment(description, amount)
    payments.append(payment)
    print(f"Made a payment of £{amount} at {payment.date}.\nPayment Reference\n: {description}.")
    save_to_json(payment)

def parse_json():
    try:
        # Load payments from the JSON file
        if os.path.exists(FILE) and os.path.getsize(FILE) > 0:
            with open(FILE, "r") as file:
                data = json.load(file)
                return data
        else:
            data = [] 
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        data = []  # Handle invalid JSON or missing file
        return

no_data = "\nThere is no payment data."

def display_payment(payment, index):
    print(
        f"{index}:\n\tPayment made at {payment['date']}.\n\t"
        f"Paid: £{payment['amount']}\n\t"
        f"Payment Reference: {payment['description']}.\n\tPayment ID: {payment['id']}\n"
    )

def display_payments():
    print("\nEXPENSES:\n".upper())
    data = parse_json()

    # Display payments
    if data:
        for index, payment in enumerate(data, start = 1):
            display_payment(payment, index)
    else:
        print(no_data)

def delete_payment(id):
    data = parse_json()
    
    # Find payment ID
    if data:
        for index, payment in enumerate(data, start = 1):
            if payment['id'] == id:
                payment_to_delete = payment
        
        if payment_to_delete:
            # Remove payment from JSON
            data = [payment for payment in data if payment["id"] != id]
            
            with open(FILE, "w") as file:
                json.dump(data, file, indent = 4)
            
            print(f"Payment with ID:{id} deleted successfully.")
    else:
        print(no_data)
        
def find_month(find_month):
    data = parse_json()
    find_month = int(find_month) 

    if data:
        found = False 
        total = 0 # Set a total

        for index, payment in enumerate(data, start=1):
            # Split the date 
            year, month, day = payment['date'].split('-')
            month = int(month) 
            # Get the total amount
            amount = int(payment['amount'])

            if find_month == month:
                total += amount
                display_payment(payment, index)  
                found = True  
        if not found:
            print(f"No payments were made in month {find_month}.")
        
        # Display total expendeture
        print(f"The total expendeture for {month}/{year} was £{total}\n")
    else:
        print(no_data) 