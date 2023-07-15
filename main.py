#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class StudentDatabase:
    def __init__(self):
        self.students = []

    def accept_student_details(self):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        grade = input("Enter grade: ")
        student = Student(name, roll_number, grade)
        self.students.append(student)
        print("Student details added successfully.")

    def display_student_details(self):
        if len(self.students) == 0:
            print("No student details found.")
        else:
            print("Student Details:")
            for student in self.students:
                print(f"Name: {student.name}\tRoll Number: {student.roll_number}\tGrade: {student.grade}")

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student Details:")
                print(f"Name: {student.name}\tRoll Number: {student.roll_number}\tGrade: {student.grade}")
                return
        print("Student not found.")

    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def update_student_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("Student grade updated successfully.")
                return
        print("Student not found.")

# Example usage
db = StudentDatabase()
while True:
    print("\nStudent Database")
    print("1. Add Student")
    print("2. Display Student Details")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student Grade")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        db.accept_student_details()
    elif choice == '2':
        db.display_student_details()
    elif choice == '3':
        roll_number = input("Enter roll number to search: ")
        db.search_student(roll_number)
    elif choice == '4':
        roll_number = input("Enter roll number to delete: ")
        db.delete_student(roll_number)
    elif choice == '5':
        roll_number = input("Enter roll number to update grade: ")
        new_grade = input("Enter new grade: ")
        db.update_student_grade(roll_number, new_grade)
    elif choice == '6':
        print("Thank you for using the Student Database.")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:





# In[ ]:




