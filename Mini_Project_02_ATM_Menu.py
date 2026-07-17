# ==========================================
# Project : ATM Menu
# ==========================================

print("========================================")
print("         WELCOME TO ATM")
print("========================================")

balance = 10000

print("\nChoose an Option")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("\nEnter Your Choice (1-4): "))

print("\n========================================")

if choice == 1:
    print("Available Balance =", balance)

elif choice == 2:
    amount = float(input("Enter Deposit Amount : "))
    balance = balance + amount
    print("Amount Deposited Successfully.")
    print("Updated Balance =", balance)

elif choice == 3:
    amount = float(input("Enter Withdraw Amount : "))

    if amount <= balance:
        balance = balance - amount
        print("Please Collect Your Cash.")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance!")

elif choice == 4:
    print("Thank You for Visiting Our ATM.")

else:
    print("Invalid Choice!")

print("========================================")
print("Transaction Completed")
print("========================================")