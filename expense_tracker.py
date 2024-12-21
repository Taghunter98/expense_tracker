import Payment
import argparse


class ExpenseTracker:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Track your expenses.")
        self.setup_parser()

    def setup_parser(self):
        # Add a payment
        self.parser.add_argument(
            "-a", "--add", nargs=2, metavar=("description", "amount"), help="Add a new Payment with <description> <amount>"
        )

        # Display all payments
        self.parser.add_argument(
            "-d", "--display", action="store_true", help="Displays all Payments"
        )
        
        # Delete a payment
        self.parser.add_argument(
            "-rm", "--remove", type = int, help = "Delete a payment with <id>"  
        )
        
        # Find payments made in a given month
        self.parser.add_argument(
            "-f", "--find", type = int, help = "Find Payments made in a month with <mm>"
        )
        
        # Help
        self.parser.add_argument(
            "-c", "--commands", action = "store_true", help="Shows all commands."
        )

    def run(self):
        args = self.parser.parse_args()

        if args.add:
            self.add_payment(args.add[0], args.add[1])
        elif args.display:
            self.display_payments()
        elif args.remove:
            Payment.delete_payment(args.remove)
        elif args.find:
            Payment.find_month(args.find)
        elif args.commands:
            ExpenseTracker.show_help()
        else:
            print("No valid arguments provided. Use -h for help.")

    def add_payment(self, description, amount):
        Payment.new_payment(description, amount)

    def display_payments(self):
        Payment.display_payments()
        
    def show_help():
        help_text = """
        Expense Tracker - Command Line Help\n
        Available Commands:
        -a, --add <description> <amount>      Add a new payment with the specified description and amount.
        -d, --display                         Display all payments.
        -rm, --remove <id>                    Remove a payment by its unique ID.
        -f, --find <month>                    Find payments made in a specific month i.e 1,2,3...
        -h, --help                            Show this help message.
        """
        print(help_text)


# Main Execution
if __name__ == "__main__":
    tracker = ExpenseTracker()

    # Run the CLI
    tracker.run()
