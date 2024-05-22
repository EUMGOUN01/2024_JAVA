# 기본적인 클래스 구조
# 클래스 선언 
# 객체 속성 선언 

# 참고자료 https://wikidocs.net/192016

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # 부모 클래스의 __init__ 메서드 호출
        self.employee_id = employee_id

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

# Employee 클래스의 인스턴스 생성
myEmployee = Employee("홍길동", 29, "E12345")

# Student 클래스의 인스턴스 생성
myStudent = Student("김철수", 21, "S98765", "컴퓨터 공학")

print("결과 출력: \n")

# 인스턴스의 속성 출력
print("이름:", myEmployee.name)
print("나이:", myEmployee.age)
print("직원 ID:", myEmployee.employee_id)
print("\n")

# 인스턴스의 속성 출력
print("이름:", myStudent.name)
print("나이:", myStudent.age)
print("학생 ID:", myStudent.student_id)
print("전공:", myStudent.major)

