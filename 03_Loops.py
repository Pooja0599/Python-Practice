# ==========================================
# Topic : Loops
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. for Loop
# ==========================================

print("For Loop")

for i in range(1, 6):
    print(i)

print("=" * 40)

# ==========================================
# 2. while Loop
# ==========================================

print("While Loop")

count = 1

while count <= 5:
    print(count)
    count += 1

print("=" * 40)

# ==========================================
# 3. range() Function
# ==========================================

print("range(5)")

for i in range(5):
    print(i)

print("=" * 40)

print("range(1,6)")

for i in range(1, 6):
    print(i)

print("=" * 40)

print("range(1,11,2)")

for i in range(1, 11, 2):
    print(i)

print("=" * 40)

# ==========================================
# 4. Loop Through String
# ==========================================

name = "Pooja"

for ch in name:
    print(ch)

print("=" * 40)

# ==========================================
# 5. Nested Loop
# ==========================================

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print("=" * 40)

# ==========================================
# 6. break Statement
# ==========================================

for i in range(1, 11):

    if i == 6:
        break

    print(i)

print("=" * 40)

# ==========================================
# 7. continue Statement
# ==========================================

for i in range(1, 11):

    if i == 5:
        continue

    print(i)

print("=" * 40)

# ==========================================
# 8. pass Statement
# ==========================================

for i in range(5):
    pass

print("Pass Statement Executed")

print("=" * 40)

# ==========================================
# 9. Reverse Counting
# ==========================================

for i in range(10, 0, -1):
    print(i)

print("=" * 40)

# ==========================================
# 10. Multiplication Table
# ==========================================

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("=" * 40)

print("Loops Completed Successfully.")