import json
import os

FILE_NAME = "students.json"


class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


class StudentManager:

    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                self.students = data

    def save_students(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["id"] == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Name: ")
        grade = input("Enter Grade: ")

        student = Student(student_id, name, grade)

        self.students.append(student.to_dict())
        self.save_students()

        print("Student Added Successfully")

    def update_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["id"] == student_id:
                student["name"] = input("Enter New Name: ")
                student["grade"] = input("Enter New Grade: ")
                self.save_students()
                print("Student Updated")
                return

        print("Student Not Found")

    def delete_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student Deleted")
                return

        print("Student Not Found")

    def list_students(self):
        if not self.students:
            print("No Students Found")
            return

        print("\n{:<10} {:<20} {:<10}".format(
            "ID", "NAME", "GRADE"))
        print("-" * 40)

        for student in self.students:
            print("{:<10} {:<20} {:<10}".format(
                student["id"],
                student["name"],
                student["grade"]
            ))


manager = StudentManager()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. List Students")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.update_student()

    elif choice == "3":
        manager.delete_student()

    elif choice == "4":
        manager.list_students()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")