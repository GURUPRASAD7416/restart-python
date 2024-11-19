
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount} successfully.")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")


# Main Program
def main():
    print("Welcome to Python Bank!")
    name = input("Enter account holder name: ")
    account = BankAccount(account_holder=name)

    while True:
        print("\n--- Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        elif choice == "4":
            print("Thank you for using Python Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()







