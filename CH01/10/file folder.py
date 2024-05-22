## 파일 폴더

import os

# example.txt 파일을 UTF-8 인코딩으로 열어서 읽음
with open("example.txt", encoding="utf-8") as file:
    data = file.read()
    print(data)

# 현재 작업 디렉토리 확인
directory = os.getcwd()

# 현재 작업 디렉토리의 파일 목록 출력
flist = os.listdir(directory)
print(flist)


## 파일 폴더 
## 원본 코드 내용

# with open("example.txt") as file:
#   data = file.read()
#   print(data)

# import os
# directory = os.getcwd()
# flist = os.listdir(directory)
# print(flist)