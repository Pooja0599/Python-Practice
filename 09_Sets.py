# ==========================================
# Topic : Sets
# Author : Pooja Singh
# GitHub : Pooja0599
# ==========================================

# ==========================================
# 1. Creating a Set
# ==========================================

fruits = {"Apple", "Banana", "Mango", "Orange"}
print("Original Set :", fruits)

print("=" * 40)

# ==========================================
# 2. Duplicate Values
# ==========================================

numbers = {10, 20, 30, 20, 40, 10}
print("Set After Removing Duplicates :", numbers)

print("=" * 40)

# ==========================================
# 3. Add Element
# ==========================================

fruits.add("Grapes")
print("After add() :", fruits)

print("=" * 40)

# ==========================================
# 4. Update Set
# ==========================================

fruits.update(["Pineapple", "Kiwi"])
print("After update() :", fruits)

print("=" * 40)

# ==========================================
# 5. Remove Element
# ==========================================

fruits.remove("Banana")
print("After remove() :", fruits)

print("=" * 40)

# ==========================================
# 6. Discard Element
# ==========================================

fruits.discard("Watermelon")
print("After discard() :", fruits)

print("=" * 40)

# ==========================================
# 7. Pop Element
# ==========================================

removed_item = fruits.pop()
print("Removed Item :", removed_item)
print("After pop() :", fruits)

print("=" * 40)

# ==========================================
# 8. Length of Set
# ==========================================

print("Length of Set :", len(fruits))

print("=" * 40)

# ==========================================
# 9. Membership Operator
# ==========================================

print("Apple" in fruits)
print("Mango" in fruits)

print("=" * 40)

# ==========================================
# 10. Union
# ==========================================

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union :", set1.union(set2))

print("=" * 40)

# ==========================================
# 11. Intersection
# ==========================================

print("Intersection :", set1.intersection(set2))

print("=" * 40)

# ==========================================
# 12. Difference
# ==========================================

print("Difference :", set1.difference(set2))

print("=" * 40)

# ==========================================
# 13. Loop Through Set
# ==========================================

print("Fruits in Set :")
for fruit in fruits:
    print(fruit)

print("=" * 40)

# ==========================================
# 14. Clear Set
# ==========================================

colors = {"Red", "Blue", "Green"}
print("Before clear() :", colors)

colors.clear()
print("After clear() :", colors)

print("=" * 40)

print("Sets Completed Successfully.")