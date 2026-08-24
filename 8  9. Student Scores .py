students = ["Rahul", "Priya", "Amit", "Sneha", "Karan", "Pooja", "Vikas", "Riya", "Aman", "Neha"]
marks = [72, 88, 95, 64, 49, 91, 83, 77, 58, 99]


top_idx = marks.index(max(marks))
low_idx = marks.index(min(marks))

print("Highest Marks:", students[top_idx], "with", marks[top_idx])
print("Lowest Marks:", students[low_idx], "with", marks[low_idx])