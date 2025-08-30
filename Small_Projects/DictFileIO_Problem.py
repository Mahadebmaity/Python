# Code: List of Dictionaries with Nested Dictionary from User Input
# import json
# import os  
# import string , random

# def Student_Details():
#     students = []   # list to hold multiple student dictionaries

#     if os.path.exists("Results/DFIO_P.json"):
#         with open("Results/DFIO_P.json", "r") as file:
#             try:
#                 students = json.load(file)
#             except json.JSONDecodeError:
#                 students = []  
    

#     def Detect_type():
#         user_input =input("Enter How many Student you want to add? ")
#         try:
#             int(user_input)
#             return int(user_input)
#         except ValueError:
#             try:
#                 float(user_input)
#                 print("Invalid input! Enter Number! not a fraction value!")
#                 return Detect_type()
#             except ValueError:
#                 str(user_input)
#                 print("Invalid input! Enter Number! not a String!,letter!,space!,Special character! ")
#                 return Detect_type()
            
#     n = Detect_type()
#     for i in range(n):
#         print(f"\nEnter details of student {i+1}:")
#         student = {}   # main dictionary
        
#         student["name"] = input("Enter Student Name: ")
#         Student_ID = ''.join(random.choices(string.ascii_uppercase,k=2)) + str(random.randint(100, 999))
#         print(f"{student['name']},Note down!\n\t\tYour ID:{Student_ID}")
#         student["id"] = Student_ID
#         student["Class"] = input("Enter Class/Stream: ")
        
#         # nested dictionary for marks
#         marks = {}
#         Subject_number = int(input(f"Enter How many subjects were tested?: "))
#         subjects =[]
#         Total_marks_eachsub =[]
#         Marks_Obtained =[]
#         for subject in range(0,Subject_number):
#             subject_name = input(f"Enter Subject {subject+1}: ").strip()
#             Total_marks = int(input(f"Enter Total Marks of {subject_name}:"))
#             marks_Obtained = int(input(f"Enter {subject_name} Marks Obtained:"))
#             marks[subject_name] = f"{marks_Obtained}/{Total_marks}"
#             subjects.append(subject_name)
#             Total_marks_eachsub.append(Total_marks)
#             Marks_Obtained.append(marks_Obtained)

#         student["marks"] = marks   # nesting dictionary inside student
        
#         students.append(student)   # add to list

#     # Display Result
#     print("\nAll Students Data (List of Dicts with Nested Dict):")
#     for index,stu in enumerate(students,start=1):
#         print(index , ":" , json.dumps(stu,indent=4))

#     # Save into JSON file
#     with open("Results/DFIO_P.json", "w") as f:
#         json.dump(students, f, indent=4)

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

# ----------------------------------------------------------------------------------------

def Student_Management_System():
    import json
    import os
    import string, random

    # students = []

    # ---------------- Load Data ----------------
    def load_data():
        if os.path.exists("Results/STMData.json"):
            with open("Results/STMData.json", "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []
    # students = []
    # ---------------- Save Data ----------------
    def save_data(students):
        with open("Results/STMData.json", "w") as f:
            json.dump(students, f, indent=4)

    # ---------------- Detect Type ----------------
    def Detect_type():
        user_input = input("Enter How many Student you want to add? ")
        try:
            return int(user_input)
        except ValueError:
            try:
                float(user_input)
                print("Invalid input! Enter Number! not a fraction value!")
                return Detect_type()
            except ValueError:
                print("Invalid input! Enter Number! not a String, letter, space, Special character!")
                return Detect_type()

    # ---------------- Add Student ----------------
    def add_Student(students):
        n = Detect_type()
        for i in range(n):
            print(f"\nEnter details of student {i+1}:")
            student = {}

            student["name"] = input("Enter Student Name: ")
            Student_ID = ''.join(random.choices(string.ascii_uppercase, k=2)) + str(random.randint(100, 999))
            print(f"{student['name']}, Note down!\n\t\tYour ID: {Student_ID}")
            student["id"] = Student_ID
            student["course"] = input("Enter Class/Stream: ")

            # nested dictionary for marks
            marks = {}
            Subject_number = int(input("Enter How many subjects were tested?: "))
            for subject in range(Subject_number):
                subject_name = input(f"Enter Subject {subject+1}: ").strip()
                Total_marks = int(input(f"Enter Total Marks of {subject_name}: "))
                marks_Obtained = int(input(f"Enter {subject_name} Marks Obtained: "))
                marks[subject_name] = f"{marks_Obtained}/{Total_marks}"

            student["marks"] = marks
            students.append(student)

        save_data(students)  # Save after adding
        print("Student added Successfully!")

    # ---------------- Search Student ----------------
    def Search_student(students):
        student_id = input("Enter Student ID to search: ").strip()
        for stu in students:
            if stu["id"] == student_id:
                print("🎓 Student Found:", stu)
                return
        print("❌ Student not found!")

    # ---------------- Update Marks ----------------
    def update_marks(students):
        student_id = input("Enter Student ID to update marks: ").strip()
        for stu in students:
            if stu["id"] == student_id:
                subject = input("Enter subject name to update marks: ").strip()
                if subject in stu["marks"]:
                    Total = int(input("Enter Total Marks: "))
                    new_marks = int(input(f"Enter new marks for {stu['name']} in {subject}: "))
                    stu["marks"][subject] = f"{new_marks}/{Total}"
                    save_data(students)
                    print("✅ Marks updated successfully!")
                else:
                    print("❌ Subject not found for this student!")
                return
        print("❌ Student not found!")

    # ---------------- Delete Student ----------------
    def delete_student(students):
        student_id = input("Enter Student ID to delete: ").strip()
        for stu in students:
            if stu["id"] == student_id:
                students.remove(stu)
                save_data(students)
                print(f"🗑️ Student {stu['name']} (ID: {stu['id']}) deleted successfully!")
                return
        print("❌ Student not found!")

    # ---------------- Display Students ----------------
    def display_students(students):
        if not students:
            print("⚠️ No student records found.")
            return
        print("\n📚 Student Records:")
        for stu in students:
            print(f"ID: {stu['id']} | Name: {stu['name']} | Course: {stu['course']} | Marks: {stu['marks']}")

    # ---------------- Main Menu ----------------
    def main():
        students = load_data()

        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. Search Student by ID")
            print("3. Update Student Marks")
            print("4. Display All Students")
            print("5. Exit")
            print("6. Delete Student")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                add_Student(students)
            elif choice == "2":
                Search_student(students)
            elif choice == "3":
                update_marks(students)
            elif choice == "4":
                display_students(students)
            elif choice == "5":
                print("👋 Exiting program. Goodbye!")
                break
            elif choice == "6":
                delete_student(students)
            else:
                print("❌ Invalid choice! Please try again.")

    main()


if __name__ == "__main__":
    Student_Management_System()
