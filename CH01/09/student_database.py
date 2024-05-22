students = []

def add_student(name, age, student_id, major):
    student = {
        "name": name,
        "age": age,
        "student_id": student_id,
        "major": major
    }
    students.append(student)

def print_students():
    print("학생 정보:")
    for student in students:
        print("이름:", student["name"])
        print("나이:", student["age"])
        print("학생 ID:", student["student_id"])
        print("전공:", student["major"])
        print()