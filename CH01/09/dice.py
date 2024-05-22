# 파이썬 클래스 연습 문제.
# dic 클래스 생성.
# 클래스에는 기본 값인 6인 side 속성이 포함.
# 1부터 주사위 눈수 사이의 랜덤한 숫자를 출력하는 roll_die()메서드 생성.
# 6면체 주사위를 만들어 10번 굴리세요.
# 추가로 10면체 주사위와 20면체 주사위 생성. 각 주사위를 10번 굴리세요.

import random

# 다이스 클래스 생성
class Dice:
    def __init__(self, sides=6):  ### 생성자 메서드, 기본값으로 6면체 주사위를 생성
        self.sides = sides  ### 주사위의 면 수를 설정하는 속성
        
    def roll_die(self):  ### 주사위를 굴리는 메서드
        return random.randint(1, self.sides)  ### 1에서 주어진 면 수 사이의 랜덤한 값을 반환
    

# 6면체 주사위를 만들어 10번 굴리기
six_sided_dice = Dice()  ### 기본값으로 6면체 주사위 객체 생성
print("6면체 주사위 10번 :")  ### 출력: "6면체 주사위를 10번 굴리기"
for _ in range(10):  ### 10번 반복
    print(six_sided_dice.roll_die(), end=" ")  ### 6면체 주사위를 굴려서 나온 값 출력
print("\n")  


# 추가 주사위 생성
# 10면체 주사위를 만들어 10번 굴리기
ten_sided_dice = Dice(10)  ### 면 수가 10인 주사위 객체 생성
print("10면체 주사위 10번 :")  ### 출력: "10면체 주사위를 10번 굴리기"
for _ in range(10):  # 10번 반복
    print(ten_sided_dice.roll_die(), end=" ")  ### 10면체 주사위를 굴려서 나온 값 출력
print("\n") 

# 20면체 주사위를 만들어 10번 굴리기
twenty_sided_dice = Dice(20)  ### 면 수가 20인 주사위 객체 생성
print("20면체 주사위 10번 :")  ### 출력: "20면체 주사위를 10번 굴리기"
for _ in range(10):  # 10번 반복
    print(twenty_sided_dice.roll_die(), end=" ")  ### 20면체 주사위를 굴려서 나온 값 출력


## 다른 방식(2) 스트링 사용법
six_sided_dice = Dice()
print("6면체 주사위 10번:")
print(" ".join(str(six_sided_dice.roll_die()) for _ in range(10)))
print()

ten_sided_dice = Dice(10)
print("10면체 주사위 10번:")
print(" ".join(str(ten_sided_dice.roll_die()) for _ in range(10)))
print()

twenty_sided_dice = Dice(20)
print("20면체 주사위 10번:")
print(" ".join(str(twenty_sided_dice.roll_die()) for _ in range(10)))