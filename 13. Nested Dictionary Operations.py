employee = {
    "E1": {"emp_name": "Rohan", "designation": "Manager", "dept": "HR", "salary": 70000},
    "E2": {"emp_name": "Ankit", "designation": "Developer", "dept": "IT", "salary": 60000},
    "E3": {"emp_name": "Kavita", "designation": "Analyst", "dept": "Finance", "salary": 80000},
    "E4": {"emp_name": "Suresh", "designation": "Developer", "dept": "IT", "salary": 65000},
    "E5": {"emp_name": "Meera", "designation": "Designer", "dept": "UI", "salary": 55000}
}

# Print E1
print("Details of E1:", employee["E1"])

# Department of E4
print("Department of E4:", employee["E4"]["dept"])

# Employee with highest salary
highest = "E1"
for emp_id in employee:
    if employee[emp_id]["salary"] > employee[highest]["salary"]:
        highest = emp_id

print("Highest Paid Employee:", employee[highest])

# Add new employee
employee["E6"] = {"emp_name": "Tanya", "designation": "Tester", "dept": "QA", "salary": 50000}
print("Updated Dictionary with E6:", employee)