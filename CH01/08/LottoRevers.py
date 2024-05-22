import random

# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))
    
    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음)
    lotto_numbers = set(random.sample(numbers, 6))
    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)
    
    return lotto_numbers, bonus_number

# 1부터 45까지의 숫자 리스트를 생성.
# random.sample() 함수를 사용하여 이 숫자 리스트에서 
# 중복 없이 6개의 숫자를 선택하여 세트로 변환 => 로또의 복권 번호.
# 숫자 리스트에서 임의의 숫자를 선택하여 보너스 번호를 생성.

# random.sample() 함수는 지정된 리스트에서 무작위로 지정된 수의 항목을 선택하는 데 사용. 
# 이 함수는 선택된 항목들을 중복 없이 반환.

# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers()
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)

# 100장의 로또 번호 생성하여 당첨 여부 판별 및 결과 저장
lotto_list = []
for idx in range(1, 101):
    # 100장 복권을 가져와 당첨번호와 비교
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
    
    # 로또 번호와 보너스 번호가 당첨 번호와 일치하는지 확인
    if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
        result = "1등 당첨!"
    elif lotto_numbers == winning_numbers:
        result = "2등 당첨! (보너스 번호 불일치)"
    elif len(lotto_numbers.intersection(winning_numbers)) == 5 and lotto_bonus_number == winning_bonus_number:
        result = "3등 당첨! (5개 일치 + 보너스 번호 일치)"
    elif len(lotto_numbers.intersection(winning_numbers)) == 5:
        result = "4등 당첨! (5개 일치)"
    elif len(lotto_numbers.intersection(winning_numbers)) == 4:
        result = "5등 당첨! (4개 일치)"
    else:
        result = "꽝"
    
    # 결과를 튜플로 묶어 리스트에 추가
    # lotto_list에 새로운 튜플을 추가하는데, 
    # 이 튜플은 세 가지 값 (lotto_numbers, lotto_bonus_number, result)을 가짐. 
    # 이 값들은 이전에 정의된 변수들의 값들을 각각 가짐.
    lotto_list.append((lotto_numbers, lotto_bonus_number, result))

# 결과 출력
for idx, (numbers, bonus_number, result) in enumerate(lotto_list, start=1):
    print(f"{idx}번째 로또 복권: {result}")


# 100장의 로또 번호를 생성하여 당첨 여부를 판별하고 결과를 저장.

# 먼저, lotto_list 라는 빈 리스트를 생성. 
# 이 리스트에는 각각의 로또 번호와 해당 번호의 당첨 결과가 저장.

# 100번의 반복문을 통해 각 로또 번호에 대해 당첨 여부를 판별. 반복문 안에서 다음을 수행:

# generate_lotto_numbers() 함수를 호출하여 로또 번호 세트와 보너스 번호를 생성.
 # 생성된 로또 번호와 보너스 번호를 당첨 번호와 비교하여 당첨 여부 확인.
 # 당첨 결과에 따라 해당하는 메시지를 result 변수에 할당.
 # lotto_list 리스트에 해당 로또 번호, 보너스 번호, 그리고 결과를 튜플 형태로 추가.
 # 모든 로또 번호의 결과가 lotto_list에 추가되면, 결과를 출력. 
 #각각의 로또 번호와 그에 해당하는 당첨 여부가 출력.








