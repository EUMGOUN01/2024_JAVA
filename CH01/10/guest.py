import os

# 방문자 파일 확인 함수
def check_visitors_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            print(f"첫 번째 손님의 이름은: {first_line}")
    else:
        print(f"{file_path} 파일이 존재하지 않습니다.")

# 현재 작업 디렉터리를 기준으로 파일 경로 설정
current_dir = os.getcwd()
file_name = "visitors.txt"
file_path = os.path.join(current_dir, file_name)

# 방문자 파일 생성 코드
os.makedirs(current_dir, exist_ok=True)
visitors = ["홍길동", "김철수", "이영희", "박지성", "최수정"]

with open(file_path, 'w', encoding='utf-8') as file:
    for visitor in visitors:
        file.write(visitor + '\n')

# 생성된 방문자 파일 확인
check_visitors_file(file_path)