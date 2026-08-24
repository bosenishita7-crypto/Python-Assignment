# Simple lambda to square a number
sq = lambda x: x * x
print("Square of 4 using Lambda:", sq(4))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Filtered Evens:", evens)

# Map to double each value
doubled = list(map(lambda x: x * 2, nums))
print("Mapped Doubled List:", doubled)