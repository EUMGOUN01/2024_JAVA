# 2024.05.13

# 5-3
# 게임에서 외계인을 격추했다고 합시다.
# alien_color 변수를 만들고 이 변수에 green, yellow, red 중 하나의 값을 할당.
# 외게인이 녹색인지 확인하는 if 문을 만드세요. 외계인이 녹색이라면 플레이어가 5점을 획득 했다는 메세지를 출력.
# 이 프로그램을 if 테스트를 통과하는 버전, 실패하는 버전으로 각각 만드세요.
alien_color = "green"

if alien_color == "green":
    print("플레이어가 5점을 획득했습니다!")

alien_color = "red"

if alien_color == "green":
    print("플레이어가 5점을 획득했습니다!")

# 5-4
# [5-3]과 마찬가지로 외계인 색깔 선택하고, if_else문을 만듭니다.
# 외계인이 녹색이면 플레이어가 5점을 획득했다는 메세지 출력.
# 외계인이 녹색이 아니면 플레이어가 10점을 획득했다는 메세지 출력.
#이 프로그램은 if 블록만 사용하는 버전, else 블록을 사용하는 버전으로 만드세요.
alien_color = "green"

if alien_color == "green":
    print("플레이어가 5점을 획득했습니다!")
else:
    print("플레이어가 10점을 획득했습니다!")

alien_color = "red"

if alien_color == "green":
    print("플레이어가 5점을 획득했습니다!")
else:
    print("플레이어가 10점을 획득했습니다!")

# 5-5
# [5-4]의 if-else문을 if-elif-else 문으로 바꿉니다.
# 외계인이 녹색이면 플레이어가 5점을 획득했다는 메세지 출력.
# 외계인이 노란색이면 플레이어가 10점을 획득했다는 메세지 출력.
# 외게인이 빨간색이면 플레이어가 15점을 획득했다는 메세지 출력.
# 이 프로그램은 세 가지 버전으로 만들어, 외계인의 색깔 맞는 메세지 출력.
alien_color = "green"

if alien_color == "green":
    print("플레이어가 5점을 획득했습니다.")
elif alien_color == "yellow":
    print("플레이어가 10점을 획득했습니다.")
else:
    print("플레이어가 15점을 획득했습니다.")

# 5-6
# if-elif-else문을 써서 사용자의 삶의 단계를 한 단어로 표현.
# 변수 age에 값을 할당하고 다음 작업 실행.
# 2세 미만이라면 영어(baby)라는 메세지 출력.
# 2세 이상 4세 미만인 경우 유아(toddler)라는 메세지 출력.
# 4세 이상 13세 미만인 경우 어린이(kid)라는 메세지 출력.
# 13세 이상 20세 미만인 경우 십대(teenager)라는 메세지 출력.
# 20세 이상 65세 미만인 경우 성인(adult)라는 메세지 출력.
# 63세 이상인 경우 노인(elder)이라는 메세지 출력.
age = 25

if age < 2:
    print("baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("teenager")
elif age < 65:
    print("adult")
else:
    print("elder")

# 5-8 다섯 명 이상의 사용자 이름이 포함된 리스트 제작.
# admin 이라는 이름이 포함되어야 함. 웹사이트에 로그인하는 사용자를 환영하는 코드를 만든다고 합시다.
# 리스트를 순화하면서 각 사용자에게 인사말을 출력.
# 사용자 이름이 admin안 경우 "관리자님 안녕하세요. 보고서를 확인하시겠습니까?" 같은 인사말 출력.
# 그렇지 않다면 "제이든님 안녕하세요. 다시 로그인해주셔서 감사합니다" 같은 범용 인사말 출력.

usernames = ['admin', 'alice', 'bob', 'charlie', 'daniel', 'emma']

for username in usernames:
    if username == 'admin':
        print(f"관리자님 안녕하세요. 보고서를 확인하시겠습니까?")
    else:
        print(f"{username}님 안녕하세요. 다시 로그인해주셔서 감사합니다.")

