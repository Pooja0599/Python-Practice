# ==========================================
# Project : Simple Calculator
# ==========================================

print("========================================")
print("      SIMPLE CALCULATOR")
print("========================================")

# Taking Input
num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))

# Menu
print("\nChoose an Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter Your Choice (1-4): "))

print("\n========================================")

# Conditional Statements
if choice == 1:
    print("Addition =", num1 + num2)

elif choice == 2:
    print("Subtraction =", num1 - num2)

elif choice == 3:
    print("Multiplication =", num1 * num2)

elif choice == 4:
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid Choice!")

print("========================================")
print("Thank You for Using Simple Calculator")
print("========================================")