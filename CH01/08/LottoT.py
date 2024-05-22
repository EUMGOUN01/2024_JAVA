import random

# 함수 생성
def generate_lotto_numbers():
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(1, 45))
    bonus_number = random.randint(1, 45)
    return numbers, bonus_number

# 결과를 저장할 파일 경로
file_path = "lotto_results.txt"

# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers()
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)

# 100장의 로또 번호 생성하여 당첨 여부 판별 및 결과 저장
lotto_list = []
with open(file_path, "w", encoding="utf-8") as file:  # UTF-8 인코딩으로 파일 열기
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
        lotto_list.append((lotto_numbers, lotto_bonus_number, result))
        
        # 결과를 파일에 저장
        file.write(f"{idx}번째 로또 복권: {result}\n")

# 100장의 로또 번호 출력
for idx, (numbers, bonus_number, result) in enumerate(lotto_list, start=1):
    print(f"{idx}번째 로또 복권: 번호: {numbers}, 보너스 번호: {bonus_number}, 결과: {result}")