# 2024.05.10 
# 변수명 변경 단축키 => F2

# 변수 숫자형 학습

print('hello, world!!')

age = 5
pi = 3.14 
msg = 'hello, world!'
data = [1, 2, 3]  
mask = 'everything' or 'object'
print(type(age), type(pi), type(msg), type(data), type(mask))

a=2
b=4

# 주석처리 CTRL K => C
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)

def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a ** b)


a = 3.14
b = 1
calc(a, b)


a = 5
b = 3
print(a, b)
b, a = a, b
print(a, b)


PI = 3.14

msg = 'hello, world!!!'
print(msg)

#print(msg.capitalize())
print(msg.find("1"))

#a = 'hello'
#b = 'world'

a = 'add'
b = 'bcc' 

def add(a,b):
    return a+ b
print(f'{a},{b}, {add(1,2)}!\nhahaha!')

msg = '     HI     '
print(len(msg))
print(len(msg.lstrip()))
print(len(msg))

msg = 'hello, hello, hello, hello, world'
print(msg.replace('hello', ''))
print(msg)
