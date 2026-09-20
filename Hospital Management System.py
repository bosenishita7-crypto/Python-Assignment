import datetime

# Patient Registration - Dictionary
patients = {}

name = input("Enter patient name: ")
age = int(input("Enter age: "))
disease = input("Enter disease: ")

patients[1] = {"Name": name, "Age": age, "Disease": disease}

# Appointment Scheduling - List
appointments = []

doctor = input("Enter doctor name: ")
date = input("Enter appointment date: ")

appointments.append([name, doctor, date])

# Doctor Information - Tuple
doctor_info = ("Dr. Rahul", "Cardiologist", "9876543210")
print("\nDoctor Information:", doctor_info)

# Medical Records - File Handling
with open("medical_record.txt", "w") as file:
    file.write("Patient Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("Disease: " + disease + "\n")

# Billing System - Class and Object
class Bill:
    def __init__(self, doctor_fee, medicine_fee):
        self.doctor_fee = doctor_fee
        self.medicine_fee = medicine_fee

    def total(self):
        return self.doctor_fee + self.medicine_fee

bill = Bill(500, 1000)
print("Total Bill:", bill.total())

# Report Generation
print("\n--- Hospital Report ---")
print("Patient:", patients[1])
print("Appointment:", appointments[0])
print("Bill:", bill.total())
print("Report Date:", datetime.date.today())