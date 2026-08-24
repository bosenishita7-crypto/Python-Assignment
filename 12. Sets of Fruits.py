fruits = {"apple", "banana", "mango", "orange", "grapes", "pineapple", "peach", "watermelon", "papaya", "kiwi"}
summer_fruits = {"mango", "watermelon", "lychee", "peach", "pineapple"}
winter_fruits = {"orange", "apple", "grapes", "guava", "kiwi"}

# Print sets
print("All Fruits:", fruits)
print("Summer Fruits:", summer_fruits)
print("Winter Fruits:", winter_fruits)

# Fruits in both main and winter sets
print("\nIn both Fruits & Winter set:", fruits & winter_fruits)

# Present only in summer, not in main set
print("Only in Summer Fruits:", summer_fruits - fruits)

# In seasonal sets, but missing from main set
print("Seasonal fruits not in main set:", (summer_fruits | winter_fruits) - fruits)

# Check orange
print("Is 'orange' in fruits?:", "orange" in fruits)

# Find where Pineapple is
p = "pineapple"
print("Pineapple found in:")
if p in fruits: print("- fruits")
if p in summer_fruits: print("- summer_fruits")
if p in winter_fruits: print("- winter_fruits")