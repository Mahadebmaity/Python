# Code: List of Dictionaries with Nested Dictionary from User Input
import json
import os  
import string , random
def Student_Details():
    students = []   # list to hold multiple student dictionaries

    if os.path.exists("Results/DFIO_P.json"):
        with open("Results/DFIO_P.json", "r") as file:
            try:
                students = json.load(file)
            except json.JSONDecodeError:
                students = []  
    

    def Detect_type():
        user_input =input("Enter How many Student you want to add? ")
        try:
            int(user_input)
            return int(user_input)
        except ValueError:
            try:
                float(user_input)
                print("Invalid input! Enter Number! not a fraction value!")
                return Detect_type()
            except ValueError:
                str(user_input)
                print("Invalid input! Enter Number! not a String!,letter!,space!,Special character! ")
                return Detect_type()
            
    n = Detect_type()
    for i in range(n):
        print(f"\nEnter details of student {i+1}:")
        student = {}   # main dictionary
        
        student["name"] = input("Enter Student Name: ")
        Student_ID = ''.join(random.choices(string.ascii_uppercase,k=2)) + str(random.randint(100, 999))
        print(f"{student['name']},Note down!\n\t\tYour ID:{Student_ID}")
        student["id"] = Student_ID
        student["Class"] = input("Enter Class/Stream: ")
        
        # nested dictionary for marks
        marks = {}
        Subject_number = int(input(f"Enter How many subjects were tested?: "))
        subjects =[]
        Total_marks_eachsub =[]
        Marks_Obtained =[]
        for subject in range(0,Subject_number):
            subject_name = input(f"Enter Subject {subject+1}: ").strip()
            Total_marks = int(input(f"Enter Total Marks of {subject_name}:"))
            marks_Obtained = int(input(f"Enter {subject_name} Marks Obtained:"))
            marks[subject_name] = f"{marks_Obtained}/{Total_marks}"
            subjects.append(subject_name)
            Total_marks_eachsub.append(Total_marks)
            Marks_Obtained.append(marks_Obtained)

        student["marks"] = marks   # nesting dictionary inside student
        
        students.append(student)   # add to list

    # Display Result
    print("\nAll Students Data (List of Dicts with Nested Dict):")
    for index,stu in enumerate(students,start=1):
        print(index , ":" , json.dumps(stu,indent=4))

    # Save into JSON file
    with open("Results/DFIO_P.json", "w") as f:
        json.dump(students, f, indent=4)

# Student_Details()
# --------------------------------------------------------

# Q1. Student Management System

# 👉 Problem:
# Create a program that allows the user to:
# Add multiple students (with ID, name, course, marks as nested dictionary).
# Save all data in a JSON file.
# Search for a student by ID.
# Update marks of a student.
# Display all students.

def Student_Management_System():

    def student_details():
        students =[]

        if os.path.exists("Results/STMData.json"):
                with open("Results/STMData.json","r") as file:
                    try:
                        students = json.load(file)
                    except json.JSONDecodeError:
                        students = []

        def Detect_type():
            user_input =input("Enter How many Student you want to add? ")
            try:
                int(user_input)
                return int(user_input)
            except ValueError:
                try:
                    float(user_input)
                    print("Invalid input! Enter Number! not a fraction value!")
                    return Detect_type()
                except ValueError:
                    str(user_input)
                    print("Invalid input! Enter Number! not a String!,letter!,space!,Special character! ")
                    return Detect_type()
    
        n = Detect_type()
        for i in range(n):
            print(f"\nEnter details of student {i+1}:")
            student = {}   # main dictionary
            
            student["name"] = input("Enter Student Name: ")
            Student_ID = ''.join(random.choices(string.ascii_uppercase,k=2)) + str(random.randint(100, 999))
            print(f"{student['name']},Note down!\n\t\tYour ID:{Student_ID}")
            student["id"] = Student_ID
            student["Class"] = input("Enter Class/Stream: ")
            
            # nested dictionary for marks
            marks = {}
            Subject_number = int(input(f"Enter How many subjects were tested?: "))
            subjects =[]
            Total_marks_eachsub =[]
            Marks_Obtained =[]
            for subject in range(0,Subject_number):
                subject_name = input(f"Enter Subject {subject+1}: ").strip()
                Total_marks = int(input(f"Enter Total Marks of {subject_name}:"))
                marks_Obtained = int(input(f"Enter {subject_name} Marks Obtained:"))
                marks[subject_name] = f"{marks_Obtained}/{Total_marks}"
                subjects.append(subject_name)
                Total_marks_eachsub.append(Total_marks)
                Marks_Obtained.append(marks_Obtained)

            student["marks"] = marks   # nesting dictionary inside student
            
            students.append(student)   # add to list

            # Save into JSON file
        with open("Results/DFIO_P.json", "w") as f:
            json.dump(students, f, indent=4)

    


Student_Management_System()