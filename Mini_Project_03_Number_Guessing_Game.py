# ==========================================
# Project : Number Guessing Game
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

print("==========================================================")
print("Number Guessing Game")
print("==========================================================")

secret_number = 7
attempt = 1

while attempt <= 3:

    guess = int(input("Enter Your Guess (1 - 10) : "))

    if guess == secret_number:
        print("Congratulations! You Guessed the Correct Number.")
        break

    elif guess < secret_number:
        print("Too Low! Try Again.")

    else:
        print("Too High! Try Again.")

    attempt += 1

if attempt > 3:
    print("\nGame Over!")
    print("The Correct Number Was :", secret_number)


print("==========================================================")
print("Thank You for Playing !")
print("==========================================================")