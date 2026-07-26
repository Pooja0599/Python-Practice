# ==========================================
# Project : Password Validator
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

print("===========================================")
print("        PASSWORD VALIDATOR")
print("===========================================")


def check_password(password):

    if len(password) < 8:
        return "Weak Password (Minimum 8 characters required)"

    elif password.isalpha():
        return "Password should contain at least one number"

    elif password.isdigit():
        return "Password should contain at least one alphabet"

    else:
        return "Strong Password"


password = input("Enter Your Password : ")

result = check_password(password)

print("===========================================")
print("Result :", result)
print("===========================================")

print("Project Completed Successfully.")