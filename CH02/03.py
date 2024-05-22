# 2024.05.10 75p~

data = [1, 2, 3, 3]
print(data, type(data))

#data = list()
#print(data, type(data))

print(data[0])
print(data[1])
print(data[2])
print(len(data))

data.append(6)
data.append(7)
data.append(8)
data.append(9)
data.append(10)
print(data, len(data))

data[3] = 4
data[4] = 5
print(data, len(data), sum(data), min(data), max(data))

data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data = list(range(10, 0, -1))
print(data, type(data))

# 10
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# 합계를 구하시오. 정렬하시오. 최대값을 찾으시오! 최솟값을 찾으시오!
data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 합계 구하기
total = sum(data)
print("합계:", total)

# 정렬하기
sorted_numbers = sorted(data)
print("정렬된 숫자:", sorted_numbers)

# 최대값 찾기
max_value = max(data)
print("최대값:", max_value)

# 최솟값 찾기
min_value = min(data)
print("최솟값:", min_value)


data = [1,2,3,4,5]
print(data[len(data)-1])
print(data[::-1])

msg = 'age'
print(msg == msg[::-1])



