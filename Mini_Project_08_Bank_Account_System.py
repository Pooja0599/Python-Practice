# ==========================================
# Project : Bank Account System
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit Money
    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully.")
        else:
            print("Invalid Amount.")

    # Withdraw Money
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid Amount.")

        elif amount > self.balance:
            print("Insufficient Balance.")

        else:
            self.balance -= amount
            print("Withdrawal Successful.")

    # Check Balance
    def check_balance(self):

        print("Account Holder :", self.account_holder)
        print("Current Balance :", self.balance)


# ==========================================
# Main Program
# ==========================================

name = input("Enter Account Holder Name : ")

account = BankAccount(name)

while True:

    print("\n========== BANK MENU ==========")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":

        amount = float(input("Enter Deposit Amount : "))
        account.deposit(amount)

    elif choice == "2":

        amount = float(input("Enter Withdrawal Amount : "))
        account.withdraw(amount)

    elif choice == "3":

        account.check_balance()

    elif choice == "4":

        print("\nThank You for Using Bank Account System.")
        break

    else:

        print("Invalid Choice. Please Try Again.")