# ==========================================
# Topic : Conditional Statements
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Simple if Statement
# ==========================================

age = 20

if age >= 18:
    print("Eligible for Voting")

print("==================================")

# ==========================================
# 2. if-else Statement
# ==========================================

num = 15

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("==================================")

# ==========================================
# 3. if-elif-else Statement
# ==========================================

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

print("==================================")

# ==========================================
# 4. Nested if
# ==========================================

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

print("==================================")

# ==========================================
# 5. Logical Operators with if
# ==========================================

age = 25
salary = 50000

if age >= 21 and salary >= 30000:
    print("Eligible for Loan")

print("==================================")

city = "Delhi"

if city == "Delhi" or city == "Mumbai":
    print("Metro City")

print("==================================")

is_logged_in = False

if not is_logged_in:
    print("Please Login")

print("==================================")

# ==========================================
# 6. Pass Statement
# ==========================================

number = 10

if number > 0:
    pass

print("Pass Statement Executed")

print("==================================")

# ==========================================
# 7. Match Case 
# ==========================================

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend")

print("==================================")

print("Conditional Statements Completed Successfully.")