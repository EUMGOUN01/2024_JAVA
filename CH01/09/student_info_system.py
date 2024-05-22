student_data = []

def add_student(name, age, student_id, major):
    student_info = f"Name: {name}, Age: {age}, Student ID: {student_id}, Major: {major}"
    student_data.append(student_info)

def print_students():
    print("학생 정보:")
    for student_info in student_data:
        print(student_info)