emp_tuple = (
    "John", "Sara", "Mike", "John", "Anna", "Sara", "David", "Paul",
    "John", "Emma", "Lisa", "Mike", "Tom", "Jack", "Sara", "Kate",
    "Leo", "John", "Maya", "Nick"
)

# Frequency of each name
print("--- Employee Name Counts ---")
for name in set(emp_tuple):
    print(name, ":", emp_tuple.count(name))

# Distinct employee list
unique_emp = tuple(set(emp_tuple))
print("\nUnique employee count:", len(unique_emp))

# Employee appearing the most
top_emp = max(unique_emp, key=emp_tuple.count)
print("Most repeated employee:", top_emp)

# Alphabetical order
print("Sorted names:", tuple(sorted(emp_tuple)))

# Search name
search = input("\nEnter name to search: ")
if search in emp_tuple:
    print(search, "is present in the tuple.")
else:
    print(search, "is not in the tuple.")