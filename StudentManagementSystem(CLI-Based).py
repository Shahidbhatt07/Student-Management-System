class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student details
        self.courses = []  # List to store course dictionaries

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        department = input("Enter department: ")
        if roll_number in self.students:
            print("Student with this roll number already exists!")
        else:
            self.students[roll_number] = {
                "name": name,
                "department": department,
                "courses": {}
            }
            print(f"Student {name} added successfully!")

    def add_course(self):
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        for course in self.courses:
            if course["code"] == course_code:
                print("Course with this code already exists!")
                return
        self.courses.append({
            "code": course_code,
            "name": course_name,
            "credits": credits
        })
        print(f"Course {course_name} added successfully!")

    def enroll_student(self):
        roll_number = input("Enter student roll number: ")
        course_code = input("Enter course code: ")
        if roll_number not in self.students:
            print("Student not found!")
            return
        if course_code not in [course["code"] for course in self.courses]:
            print("Course not found!")
            return
        self.students[roll_number]["courses"][course_code] = {"grade": "Not Graded"}
        print(f"Student {self.students[roll_number]['name']} enrolled in {course_code}")

    def assign_grade(self):
        roll_number = input("Enter student roll number: ")
        course_code = input("Enter course code: ")
        grade = input("Enter grade: ")
        if roll_number not in self.students:
            print("Student not found!")
            return
        if course_code not in self.students[roll_number]["courses"]:
            print("Student is not enrolled in this course!")
            return
        self.students[roll_number]["courses"][course_code]["grade"] = grade
        print(f"Grade {grade} assigned to {self.students[roll_number]['name']} for {course_code}")

    def display_student(self):
        roll_number = input("Enter student roll number: ")
        if roll_number not in self.students:
            print("Student not found!")
            return
        student = self.students[roll_number]
        print(f"\nStudent Name: {student['name']}")
        print(f"Roll Number: {roll_number}")
        print(f"Department: {student['department']}")
        print("Courses Enrolled:")
        for course_code, details in student["courses"].items():
            print(f"  {course_code}: Grade - {details['grade']}")

    def list_all_students(self):
        print("\nList of all students:")
        for roll_number, student in self.students.items():
            print(f"{roll_number}: {student['name']} ({student['department']})")

    def list_all_courses(self):
        print("\nList of all courses:")
        for course in self.courses:
            print(f"{course['code']}: {course['name']} ({course['credits']} Credits)")


# Main program
sms = StudentManagementSystem()
while True:
    print("\n1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Assign Grade")
    print("5. Display Student Record")
    print("6. List All Students")
    print("7. List All Courses")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.add_course()
    elif choice == "3":
        sms.enroll_student()
    elif choice == "4":
        sms.assign_grade()
    elif choice == "5":
        sms.display_student()
    elif choice == "6":
        sms.list_all_students()
    elif choice == "7":
        sms.list_all_courses()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
