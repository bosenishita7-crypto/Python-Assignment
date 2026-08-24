class Student:
    def __init__(self, name, dept, roll):
        self.name = name
        self.dept = dept
        self.roll = roll

    def show(self):
        print(f"Roll: {self.roll} | Name: {self.name} | Dept: {self.dept}")

# Create 5 students
s1 = Student("Aarav", "CSE", 101)
s2 = Student("Diya", "ECE", 102)
s3 = Student("Kabir", "IT", 103)
s4 = Student("Simran", "ME", 104)
s5 = Student("Varun", "CE", 105)

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()