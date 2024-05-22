# 2024.05.13 p.93~

data = [1, 2, 3]
for d in data:
    print(d, end=' ')
data[1] = 5
print('-', data[1])

string = 'hello'
for s in string:
    print(s, end=' ')
#string[1] = 'E'
print('-', string[1])

data = (1, 2, 3)
print(data, type(data))
for i in data:
    print(i)
#data[1] = 5

data2 = [i**2 for i in data if i**2 < 5]
print(data2, type(data2))

data3 = []
for i in data:
    if i**2 < 5:
        data3.append(i**2)
print(data3)


# range(1, 11) - 1부터 10까지
# sum, min, max, average



numbers = range(1, 11)
total = sum(numbers)
minimum = min(numbers)
maximum = max(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Min:", minimum)
print("Max:", maximum)
print("Average:", average)


# 리스트 복사하기.

#CH05
score = 70


if (90 <= score) and (score < 100):
    print('A')
elif (80 <= score) and (score < 90):
    print('B')
else:
    print('F')

a = 5
if a == 5:
    print('right!')

msg = 'hello'
if msg == 'hello':
    print('right!')

data = [1, 2, 3]
if data == [1, 2, 3]:
    print('right!')

if []:
    print('right!!!')

data = [1, 2, 3]
if 4 in data:
    print('Here!')

string = 'hello'
if 'e' in string:
    print('Here!')


# 조건문.

