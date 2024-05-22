# 파이썬 리스트 튜플 문제
# 복권 만들기
# 10개의 숫자와 5개의 문자를 포함하는 리스트나 튜플을 만드세요.
# 리스트에서 숫자나 문자를 임의로 4개 선택.
# 이와 일치하는 티켓에 상금을 지급한다는 메세지 출력.

# 참고자료(1) https://wikidocs.net/106795


import random  # 랜덤 모듈 임포트

# 복권 번호 생성
numbers = [i for i in range(1, 11)]  # 1부터 10까지의 숫자
letters = ['A', 'B', 'C', 'D', 'E']  # 5개의 문자

# 복권 티켓 생성
tickets = [(random.sample(numbers, 4), random.sample(letters, 1)) for _ in range(10)]
# 10개의 복권 티켓 생성. 각각은 숫자 4개와 문자 1개로 이루어져 있음.
# random.sample 함수를 사용하여 numbers 리스트에서 4개의 숫자를, letters 리스트에서 1개의 문자를 무작위로 선택하여 티켓 생성.


# ramdom. 모듈 사용하기 = > https://www.daleseo.com/python-random/
# 당첨 번호 선택
winning_numbers = random.sample(numbers, 4)  # 4개의 당첨 숫자를 무작위 선택.
winning_letter = random.choice(letters)  # 당첨 문자를 무작위 선택

# 당첨 확인
# 우승 티켓들을 저장할 빈 리스트를 생성.
winning_tickets = []
# 'tickets' 리스트에서 각 티켓과 해당하는 문자 순회.
for ticket, letter in tickets:
    # 현재 티켓이 우승 번호와 우승 문자와 일치하는지 확인.
    if ticket == winning_numbers and letter == winning_letter:
        # 일치하는 경우, 해당 티켓을 'winning_tickets' 리스트에 추가.
        # 추가할 때에는 튜플로 묶어서 추가.
        winning_tickets.append((ticket, letter))
# 생성된 티켓들과 당첨 번호 및 당첨 문자를 비교하여 당첨된 티켓 찾음.

# 당첨 확인
# 리스트 내포와 for문을 사용.
# winning_tickets = [(ticket, letter) for ticket, letter in tickets if ticket == winning_numbers and letter == winning_letter]

# 결과 출력
print("당첨 번호:", winning_numbers, "당첨 문자:", winning_letter)  # 당첨 번호와 당첨 문자 출력
if winning_tickets:
    print("축하합니다! 당첨 티켓을 찾았습니다!")
    for ticket, letter in winning_tickets:
        print("당첨 티켓 번호:", ticket, "당첨 티켓 문자:", letter)
else:
    print("아쉽지만 당첨 티켓을 찾지 못했습니다. 다음 기회에 다시 시도해보세요!")