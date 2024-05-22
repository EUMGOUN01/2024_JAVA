class Dog :
    """개를 표현하는 클래스"""

    def __int__(self, name, age):
     """name과 age 속성 초기화"""
     self.name = name
     self.age = age
     self.city = "busan"

     def sit(self):
        """개가 앉기 동작"""
        print(f"개가 앉기 {self.name}")

myDog = Dog("hong", 10)
myDog.sit()

# https://codermun-log.tistory.com/73 참고