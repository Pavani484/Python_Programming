
import random
import datetime

# --------------------- Data Structures ---------------------
programs = {}         # program_id: {"name":..., "courses": {...}}
students = {}         # student_id: {"name":..., "program_id":..., "courses": [...], "hall_ticket":...}
exam_fee_paid = {}    # student_id: True/False
exam_timetable = {}   # course_code: date
attendance = {}       # course_code: {date: [student_ids]}
marks = {}            # student_id: {course_code: marks}

# --------------------- Functions ---------------------
def enter_program():
    program_id = input("Enter Program ID: ")
    name = input("Enter Program Name: ")
    programs[program_id] = {"name": name, "courses": {}}
    print("Program added successfully!\n")

def enter_course():
    program_id = input("Enter Program ID: ")
    if program_id not in programs:
        print("Program not found!")
        return
    semester = input("Enter Semester: ")
    course_code = input("Enter Course Code: ")
    course_name = input("Enter Course Name: ")
    programs[program_id]["courses"][course_code] = {"name": course_name, "semester": semester}
    print("Course added successfully!\n")

def enter_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    program_id = input("Enter Program ID: ")
    if program_id not in programs:
        print("Program not found!")
        return
    students[student_id] = {"name": name, "program_id": program_id, "courses": [], "hall_ticket": ""}
    print("Student added successfully!\n")

def generate_hall_tickets():
    for student_id, info in students.items():
        if not info["hall_ticket"]:
            info["hall_ticket"] = f"HT{random.randint(1000,9999)}"
    print("Hall tickets generated!\n")

def student_program_mapping():
    for student_id, info in students.items():
        print(f"{student_id} -> {programs[info['program_id']]['name']}")

def student_course_mapping():
    for student_id, info in students.items():
        program_courses = list(programs[info['program_id']]['courses'].keys())
        info['courses'] = program_courses
        print(f"{students[student_id]['name']} mapped to courses: {info['courses']}")

def collect_exam_fee():
    for student_id in students.keys():
        exam_fee_paid[student_id] = True
    print("Exam fees collected!\n")

def exam_timetable_mapping():
    n = int(input("How many exams to schedule? "))
    for _ in range(n):
        course_code = input("Enter Course Code: ")
        date_str = input("Enter Exam Date (YYYY-MM-DD): ")
        exam_timetable[course_code] = date_str
    print("Exam timetable mapped!\n")

def generate_attendance():
    for course_code in exam_timetable.keys():
        attendance[course_code] = {}
        n = int(input(f"How many dates for {course_code}? "))
        for _ in range(n):
            date = input("Enter date (YYYY-MM-DD): ")
            present_students = input("Enter present student IDs separated by comma: ").split(",")
            attendance[course_code][date] = present_students
    print("Attendance recorded!\n")

def enter_marks():
    for student_id, info in students.items():
        marks[student_id] = {}
        for course_code in info["courses"]:
            m = float(input(f"Enter marks for {info['name']} in {course_code}: "))
            marks[student_id][course_code] = m
    print("Marks entered!\n")

def results_generation():
    print("\n--- Results ---")
    for student_id, info in students.items():
        total = 0
        count = 0
        failed = False
        for course_code, m in marks[student_id].items():
            if m < 40:
                failed = True
        if failed:
            print(f"{info['name']} : F")
        else:
            total = sum(marks[student_id].values())
            count = len(marks[student_id])
            avg = total / count
            print(f"{info['name']} : Total = {total}, Average = {avg:.2f}")

# --------------------- Main Menu ---------------------
while True:
    print("""
1. Enter Program details
2. Enter Course details
3. Enter Student details
4. Generate Hall Ticket numbers
5. Student - Program mapping
6. Student - Course mapping
7. Collect Exam fee
8. Exam Time Table mapping
9. Generate Attendance sheet
10. Enter Marks
11. Results Generation
12. Exit
""")
    choice = input("Enter choice: ")
    if choice == "1":
        enter_program()
    elif choice == "2":
        enter_course()
    elif choice == "3":
        enter_student()
    elif choice == "4":
        generate_hall_tickets()
    elif choice == "5":
        student_program_mapping()
    elif choice == "6":
        student_course_mapping()
    elif choice == "7":
        collect_exam_fee()
    elif choice == "8":
        exam_timetable_mapping()
    elif choice == "9":
        generate_attendance()
    elif choice == "10":
        enter_marks()
    elif choice == "11":
        results_generation()
    elif choice == "12":
        break
    else:
        print("Invalid choice!")
