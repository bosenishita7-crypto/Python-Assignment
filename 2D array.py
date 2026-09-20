# Q21: 2D array (list of lists) to store marks of 3 subjects of 5 students
# Rows = students (0 to 4), Columns = subjects (0 to 2)

marks = [
    [45, 78, 90],
    [60, 55, 40],
    [88, 92, 76],
    [30, 65, 85],
    [70, 48, 60]
]

rows = len(marks)      # 5 students
cols = len(marks[0])   # 3 subjects

# i. Find the maximum marks (overall)
max_marks = marks[0][0]
for i in range(rows):
    for j in range(cols):
        if marks[i][j] > max_marks:
            max_marks = marks[i][j]
print("i. Maximum marks overall =", max_marks)

# ii. Find the minimum marks (overall)
min_marks = marks[0][0]
for i in range(rows):
    for j in range(cols):
        if marks[i][j] < min_marks:
            min_marks = marks[i][j]
print("ii. Minimum marks overall =", min_marks)

# iii. Find average marks (overall)
total = 0
for i in range(rows):
    for j in range(cols):
        total += marks[i][j]
average = total / (rows * cols)
print("iii. Average marks overall = %.2f" % average)

# iv. Find the maximum marks subject-wise
print("iv. Maximum marks subject-wise:")
for j in range(cols):
    max_sub = marks[0][j]
    for i in range(1, rows):
        if marks[i][j] > max_sub:
            max_sub = marks[i][j]
    print(f"   Subject {j+1} -> {max_sub}")

# v. Find average marks subject-wise
print("v. Average marks subject-wise:")
for j in range(cols):
    sub_sum = 0
    for i in range(rows):
        sub_sum += marks[i][j]
    print(f"   Subject {j+1} -> {sub_sum/rows:.2f}")

# vi. Find the student id (0 to 4) who scored max marks in sub 1 (index 0)
sub_index = 0  # sub 1
best_student = 0
for i in range(1, rows):
    if marks[i][sub_index] > marks[best_student][sub_index]:
        best_student = i
print("vi. Student with max marks in sub 1 =", best_student)

# vii. Add 10 marks for all students who scored less than 50 in sub 1 (col 0)
for i in range(rows):
    if marks[i][0] < 50:
        marks[i][0] += 10
print("vii. Marks updated (added 10 where sub1 < 50):", marks)

# viii. Find no. of students who scored more than 80 in sub 2 (col 1)
count = 0
for i in range(rows):
    if marks[i][1] > 80:
        count += 1
print("viii. Students scoring >80 in sub 2 =", count)

# ix. Find the minimum marks of student 2 (3rd row -> index 2)
min_stu = min(marks[2])
print("ix. Minimum marks of student 2 =", min_stu)

# x. Find the maximum marks of student 4 (index 4)
max_stu = max(marks[4])
print("x. Maximum marks of student 4 =", max_stu)