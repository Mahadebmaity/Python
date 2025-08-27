import os
import json
import pickle
# Dictionary concept
# student = {
#     "id": 101,
#     "name": "Madhurima Maity",
#     "course": "MCA",
#     "CGPA": 8.9
# }

# Access element of student dict
# student["id"] = 105 #change value
# print(student["id"])
# print(student.get("id")) # access value in diffrent way

# print(student.keys()) #only keys print
# print(student.values()) # only values are printed
# print(student.items()) # all items are printed


# for key, value in student.items():
#     print(key, ":", value)


# ------------------------------------------------
#file io with dictionary 
#-------------------------------------------------
#store value specific folder file path
# with open(r"C:\Users\Mahadeb Maity\OneDrive\Python\Beginners_Python\practiceMode\student.txt","w") as file:
#     file.write(str(student))


#store value another folder file path
# with open("Module1/student.txt","w") as file:
#     file.write(str(student))


#if not exist file then create  using os module
# # Desired directory
# folder = r"C:\Users\Mahadeb Maity\OneDrive\Python\Beginners_Python\Results"
# # Create directory if it doesn’t exist
# os.makedirs(folder,exist_ok=True)
# # full path for file
# file_path = os.path.join(folder,"studentRes.txt")
# # store
# with open(file_path,"w") as file:
#     file.write(str(student))

# ----------------------------------------------------

# Using str() and eval()
# (Saves dictionary as plain text)
# with open("Results/student.txt", "w") as f:
#     f.write(str(student))
# with open("Results/student.txt", "r") as f:
#     data = f.read()
#     student_dict = eval(data)   # Convert string back to dictionary
# print(student_dict)
# -----------------------------------------------------

# using JSON
# write only
# with open("Results/student.json", "w") as f:
#     json.dump(student,f,indent=4)
    # json.dump(student,f)   # dump dictionary into file
# read only
# with open("Results/student.json", "r") as f:
#     data = json.load(f)     # load dictionary from file
# print(data)


# ---------------------------------------------------------
# Additional knowledge outoff this topic
# print text centered in the console.

# 1. Using str.center(width)
# text = "Hello Mahadeb!"
# print(text.center(50))   # 50 is total width
# print("Welcome Mahadeb!".center(100))

# # Center According to Terminal Width (Dynamic)
# import shutil
# text = "Hello Guys!"
# greetings = shutil.get_terminal_size().columns
# print(text.center(greetings))
# print(text.center(greetings,"-")) # as your wish 

# -------------------------------------------------------------
# Using pickle Module (Binary Format)
# Pickle is used for saving Python objects in binary form

# with open("Results/student.pkl", "wb") as f: #just for checking not requirement 
#     pickle.dump(student, f) 

# with open("Results/student.pkl", "rb") as f: # just read pickle file and print this to read human
#     data = pickle.load(f)
# print(data)

# ---------------------------------------------------------------
# ✅ Append Multiple Records (List of Dicts)
# students = [
#     {"id": 101, "name": "Mahadeb", "course": "MCA", "marks": 89},
#     {"id": 102, "name": "Sita", "course": "BCA", "marks": 92}
# ]

# with open("Results/students.json", "w") as f:
#     json.dump(students, f,indent=4)
# read data in file and print data 
# with open("Results/students.json", "r") as f:
#     data = json.load(f)
#     for stu in data:
#         print(stu["name"],"ID",stu["id"],"Course",stu["course"],"scored", stu["marks"])

# Update Dictionary in File
# Update student marks
# for stu in students:
#     if stu["id"] == 101:
#         stu["marks"] = 95

# Write back updated data
# with open("Results/students.json", "w") as f:
#     json.dump(students, f, indent=4)

# read data in file and print data after update marks 
# with open("Results/students.json", "r") as f:
#     students = json.load(f)
#     # for stu in students:
#     #     print(stu["name"],"ID",stu["id"],"Course",stu["course"],"scored", stu["marks"])
# roll = 103
# found = False 
# for stu in students:
#     if stu["id"] == roll:
#         print("Found:", stu)
#         found = True
#         break

# if not found:
#     print(f"Roll:{roll}\nstudent data Not Found!")

# -----------------------------------------------------------------------
# # user input using string 
# student = {}   # empty dictionary

# # taking inputs from user
# student["id"] = int(input("Enter Student ID: "))
# student["name"] = input("Enter Student Name: ")
# student["course"] = input("Enter Course: ")
# student["CGPA"] = float(input("Enter CGPA: "))

# print("\nStudent Dictionary:")
# print(student)

# with open("Results/input_students.json", "w") as file:
#     json.dump(student,file,indent=4)

# ------------------------------------------------------------------------
# store multiple student data
# students = []   # list to hold multiple student dictionaries

# n = int(input("How many students? "))

# for i in range(n):
#     print(f"\nEnter details of student {i+1}:")
#     student = {}
#     student["id"] = int(input("Enter Student ID: "))
#     student["name"] = input("Enter Student Name: ")
#     student["course"] = input("Enter Course: ")
#     student["CGPA"] = float(input("Enter CGPA: "))
#     students.append(student)

# print("\nAll Students Data:")
# for stu in students:
#     print(stu)
# ---------------------------------------------------------------------
# Now I write how to multiple data store as a list of dictionary 

import shutil
import os

# Greeting line
Greetings = shutil.get_terminal_size().columns
print("Good Morning Friends".center(Greetings, "*"))
print("Employee Details!")

Total_Employee = []

if os.path.exists("Results/Employee.json"):
    with open("Results/Employee.json", "r") as file:
        try:
            Total_Employee = json.load(file)
        except json.JSONDecodeError:
            Total_Employee = []   

Number_of_Employee = int(input("Enter how many employee data you want to add now? "))

for i in range(Number_of_Employee):
    print(f"\nNow enter Employee {i+1} details:")
    Employee = {}
    Employee["Name"] = input("Enter Employee Name: ")
    Employee["ID"] = int(input(f"Enter Emp.{Employee['Name']} ID: "))
    Employee["Age"] = int(input(f"Enter Emp.{Employee['Name']} Age: "))
    Employee["PhNo"] = input(f"Enter Emp.{Employee['Name']} Phone number: ")  # string
    Total_Employee.append(Employee)

# Display all data
print("\nDisplay All Data")
for index, emp in enumerate(Total_Employee, start=1):
    print(index, ":", json.dumps(emp, indent=4))

# Save JSON file 
with open("Results/Employee.json", "w") as file:
    json.dump(Total_Employee, file, indent=4)

# -----------------------------------------------------------------------------


