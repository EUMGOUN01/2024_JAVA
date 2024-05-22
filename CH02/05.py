# 2024.05.13 연습문제

# 4-3
# for 루프를 사용해 1에서 20까지 숫자 출력.
for i in range(1, 21):
    print(i)

# 4-4
# 1에서 백만까지 숫자 리스트 만들고, for 루프를 써서 출력.
numbers = list(range(1, 1000001))
for number in numbers:
    print(number)

# 4-5
# 1에서 백만까지 숫자 리스트 만들고, min(), max()를 써서 리스트가 실제로 1에서 시작되고 백만에서 끝나는지 확인.
# sum() 함수를 써서 파이썬이 이들을 얼마나 빨리 더하는지 보세요.
# 1에서 백만까지 숫자 리스트 만들기
numbers = list(range(1, 1000001))

# 리스트가 실제로 1에서 시작되고 백만에서 끝나는지 확인
print("최솟값:", min(numbers))
print("최댓값:", max(numbers))

# sum() 함수를 사용하여 더하는 시간 측정
import time

start_time = time.time()
total = sum(numbers)
end_time = time.time()

print("합:", total)
print("총 소요된 시간:", end_time - start_time, "초")

# 4-6 
# range() 함수의 세번째 인수를 써서 1에서 20까지의 홀수 리스트 제작. for 루프를 사용해 각 숫자 출력.
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

# 4-7
# 3에서 30까지 3의 배수 리스트를 만드세요. for 루프 써서 각 숫자 출력.
multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)

# 4-8
# 자신을 세번 곱한 숫자를 세제곱이라 부름.
# 2의 세제곱은 2**3으로 계산. 1에서 10까지의 정수 세제곱 리스트 제작. for 루프를 써서 각 값을 출력.
cubed_numbers = [x ** 3 for x in range(1, 11)]
for number in cubed_numbers:
    print(number)

# 4-9
# [4-8]을 리스트 내포 문법으로 만드시오.
cubed_numbers = [x ** 3 for x in range(1, 11)]
print(cubed_numbers)

# 4-10
# 메세지 "리스트의 첫 세 항목은" 출력. 슬라이스를 사용해 해당 프로그램의 리스트 처음 세 요소를 출력.
# 메세지 "리스트의 중간 항목은" 출력. 슬라이스를 사용해 해당 프로그램의 리스트 중간 세 요소를 출력.
# 메세지 "리스트의 마지막 항목은" 출력. 슬라이스를 사용해 해당 프로그램의 리스트 마지막 세 요소를 출력.

# 5-2 조건 테스트
# 문자열에 대한 동일서 테스트와 비동일성 테스트
# lower() 메서드를 사용한 테스트
# 일치, 불일치, 이상, 이하, 초과, 미만이 모두 포함된 산술 비교 테스트
# and 키워드와 or 키워드를 사용한 테스트
# 요소가 리스트에 있는지 확인하는 테스트
# 요소가 리스트에 없는지 확인하는 테스트

# 문자열에 대한 동일성 테스트와 비동일성 테스트
string1 = "hello"
string2 = "world"
if string1 == string2:
    print("문자열이 동일합니다.")
else:
    print("문자열이 동일하지 않습니다.")

# lower() 메서드를 사용한 테스트
string3 = "Hello"
string4 = "hello"
if string3.lower() == string4.lower():
    print("대소문자를 무시하면 문자열이 동일합니다.")
else:
    print("대소문자를 무시하면 문자열이 동일하지 않습니다.")

# 산술 비교 테스트
num1 = 10
num2 = 5
if num1 == num2:
    print("두 숫자가 같습니다.")
elif num1 != num2:
    print("두 숫자가 다릅니다.")
elif num1 > num2:
    print("num1이 num2보다 큽니다.")
elif num1 >= num2:
    print("num1이 num2보다 크거나 같습니다.")
elif num1 < num2:
    print("num1이 num2보다 작습니다.")
elif num1 <= num2:
    print("num1이 num2보다 작거나 같습니다.")

# and 와 or 키워드를 사용한 테스트
if string1 == "hello" and string2 == "world":
    print("두 문자열이 각각 'hello'와 'world'입니다.")
elif string1 == "hello" or string2 == "world":
    print("두 문자열 중 적어도 하나가 'hello' 또는 'world'입니다.")

# 요소가 리스트에 있는지 확인하는 테스트
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("리스트에 숫자 3이 있습니다.")

# 요소가 리스트에 없는지 확인하는 테스트
if 6 not in my_list:
    print("리스트에 숫자 6이 없습니다.")

