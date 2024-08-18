import os
import hashlib

# File path where customer details will be saved
customer_file = "customers.txt"

def hash_pin(pin):
    """Hash the user's PIN for security."""
    return hashlib.sha256(pin.encode()).hexdigest()

def load_customers():
    """Load customer data from the file."""
    if not os.path.exists(customer_file):
        return {}
    customers = {}
    with open(customer_file, 'r') as file:
        for line in file:
            hashed_pin, balance = line.strip().split('\t')
            customers[hashed_pin] = float(balance)
    return customers

def save_customers(customers):
    """Save customer data to the file."""
    with open(customer_file, 'w') as file:
        for hashed_pin, balance in customers.items():
            file.write(f"{hashed_pin}\t{balance}\n")

def print_colored(text, color_code):
    """Print colored text to the console."""
    print(f"\033[{color_code}m{text}\033[0m")

def welcome_screen():
    """Display the welcome screen."""
    print_colored("╔════════════════════════════════════════╗", "96")
    print_colored("║       Welcome to Python Bank           ║", "96")
    print_colored("╠════════════════════════════════════════╣", "96")
    print_colored("║ 1) Register                            ║", "93")
    print_colored("║ 2) Log In                              ║", "93")
    print_colored("║ 3) Exit                                ║", "93")
    print_colored("╚════════════════════════════════════════╝", "96")

def main_menu():
    """Display the main menu."""
    print_colored("\n╔════════════════════════════════════════╗", "96")
    print_colored("║        Main Menu                       ║", "96")
    print_colored("╠════════════════════════════════════════╣", "96")
    print_colored("║ 1) Deposit Money                       ║", "93")
    print_colored("║ 2) Withdraw Money                      ║", "93")
    print_colored("║ 3) Check Balance                       ║", "93")
    print_colored("║ 4) Log Out                             ║", "93")
    print_colored("╚════════════════════════════════════════╝", "96")

def register(customers):
    """Register a new user."""
    while True:
        new_pin = input("Enter a new 4-digit PIN: ")
        if len(new_pin) != 4 or not new_pin.isdigit():
            print_colored("PIN must be exactly 4 digits.", "91")
        else:
            hashed_pin = hash_pin(new_pin)
            if hashed_pin in customers:
                print_colored("This PIN is already in use. Please choose a different PIN.", "91")
            else:
                break

    while True:
        try:
            initial_deposit = float(input("Enter your initial deposit amount ₹: "))
            if initial_deposit < 0:
                print_colored("Initial deposit cannot be negative.", "91")
            else:
                break
        except ValueError:
            print_colored("Invalid input. Please enter a numeric value.", "91")

    customers[hashed_pin] = initial_deposit
    save_customers(customers)
    print_colored(f"Registration successful! Your balance is ₹{initial_deposit}", "92")

def log_in(customers):
    """Log in an existing user."""
    for _ in range(5):
        pin = input("Enter your 4-digit PIN: ")
        hashed_pin = hash_pin(pin)
        if hashed_pin in customers:
            print_colored("Login successful!", "92")
            return hashed_pin
        else:
            print_colored("Incorrect PIN. Please try again.", "91")
    print_colored("Too many failed attempts. Returning to the main menu.", "91")
    return None

def deposit(customers, user_pin):
    """Deposit money into the user's account."""
    while True:
        try:
            amount = float(input("Enter the amount to deposit ₹: "))
            if amount < 0:
                print_colored("Deposit amount cannot be negative.", "91")
            else:
                customers[user_pin] += amount
                save_customers(customers)
                print_colored(f"Deposit successful! New balance: ₹{customers[user_pin]}", "92")
                break
        except ValueError:
            print_colored("Invalid input. Please enter a numeric value.", "91")

def withdraw(customers, user_pin):
    """Withdraw money from the user's account."""
    while True:
        try:
            amount = float(input("Enter the amount to withdraw ₹: "))
            if amount < 0:
                print_colored("Withdrawal amount cannot be negative.", "91")
            elif amount > customers[user_pin]:
                print_colored("Insufficient balance.", "91")
            else:
                customers[user_pin] -= amount
                save_customers(customers)
                print_colored(f"Withdrawal successful! New balance: ₹{customers[user_pin]}", "92")
                break
        except ValueError:
            print_colored("Invalid input. Please enter a numeric value.", "91")

def check_balance(customers, user_pin):
    """Check the user's account balance."""
    balance = customers[user_pin]
    print_colored(f"Your current balance is ₹{balance}", "92")

def banking_service():
    """Main function to run the banking service."""
    customers = load_customers()
    
    while True:
        welcome_screen()
        choice = input("Please choose an option (1/2/3): ").strip()

        if choice == "1":
            register(customers)
        elif choice == "2":
            user_pin = log_in(customers)
            if user_pin:
                while True:
                    main_menu()
                    option = input("Please choose an option (1/2/3/4): ").strip()
                    
                    if option == "1":
                        deposit(customers, user_pin)
                    elif option == "2":
                        withdraw(customers, user_pin)
                    elif option == "3":
                        check_balance(customers, user_pin)
                    elif option == "4":
                        print_colored("Logging out. Thank you for using Python Bank!", "92")
                        break
                    else:
                        print_colored("Invalid option. Please try again.", "91")
        elif choice == "3":
            print_colored("Thank you for using Python Bank! Goodbye!", "92")
            break
        else:
            print_colored("Invalid option. Please try again.", "91")

# Start the banking service
if __name__ == "__main__":
    banking_service()
# Modified with CHATGPT
