import sys
import os

BALANCE_FILE = "balance.txt"

def read_balance():
    """Read current balance from file or return 0.0 if file missing/empty."""
    if not os.path.exists(BALANCE_FILE):
        return 0.0
    with open(BALANCE_FILE, "r") as f:
        content = f.read().strip()
        return float(content) if content else 0.0

def write_balance(balance):
    """Write the current balance to file."""
    with open(BALANCE_FILE, "w") as f:
        f.write(f"{balance:.2f}")

def deposit(amount):
    """Increase balance by the given amount."""
    balance = read_balance()
    balance += amount
    write_balance(balance)
    print(f"Deposited: ${amount:.2f}")
    print(f"Current Balance: ${balance:.2f}")

def withdraw(amount):
    """Decrease balance if sufficient funds."""
    balance = read_balance()
    if amount > balance:
        print("Insufficient funds.")
        return
    balance -= amount
    write_balance(balance)
    print(f"Withdrew: ${amount:.2f}")
    print(f"Current Balance: ${balance:.2f}")

def display():
    """Show current balance."""
    balance = read_balance()
    print(f"Current Balance: ${balance:.2f}")

def main():
    """Handle CLI commands."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        return

    parts = sys.argv[1].split(":")
    command = parts[0].lower()

    if command == "display":
        display()
        return

    if len(parts) != 2:
        print("Usage: python main.py <command>:<amount>")
        return

    try:
        amount = float(parts[1])
    except ValueError:
        print("Amount must be a number.")
        return

    if command == "deposit":
        deposit(amount)
    elif command == "withdraw":
        withdraw(amount)
    else:
        print("Unknown command. Use deposit, withdraw, or display.")

if __name__ == "__main__":
    main()
