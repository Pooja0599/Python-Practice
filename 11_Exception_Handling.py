# ==========================================
# Topic : Exception Handling
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Basic try-except
# ==========================================

try:
    num = int(input("Enter a Number : "))
    print("You Entered :", num)

except ValueError:
    print("Invalid Input! Please Enter Only Numbers.")

print("=" * 50)

# ==========================================
# 2. Division by Zero Exception
# ==========================================

try:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    result = a / b

    print("Result :", result)

except ZeroDivisionError:
    print("Cannot Divide by Zero.")

print("=" * 50)

# ==========================================
# 3. Multiple Exceptions
# ==========================================

try:
    number = int(input("Enter Number : "))
    result = 100 / number
    print("Result :", result)

except ValueError:
    print("Please Enter a Valid Integer.")

except ZeroDivisionError:
    print("Number Cannot Be Zero.")

print("=" * 50)

# ==========================================
# 4. try-except-else
# ==========================================

try:
    age = int(input("Enter Your Age : "))

except ValueError:
    print("Invalid Age.")

else:
    print("Your Age is :", age)

print("=" * 50)

# ==========================================
# 5. try-except-finally
# ==========================================

try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File Not Found.")

finally:
    print("Finally Block Executed.")

print("=" * 50)

# ==========================================
# 6. Raising Custom Exception
# ==========================================

try:
    marks = int(input("Enter Marks : "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks Should Be Between 0 and 100.")

    print("Marks :", marks)

except ValueError as e:
    print(e)

print("=" * 50)

# ==========================================
# 7. Exception Object
# ==========================================

try:
    num = int(input("Enter Number : "))
    print(50 / num)

except Exception as e:
    print("Error :", e)

print("=" * 50)

print("Exception Handling Completed Successfully.")