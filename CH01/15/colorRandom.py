import matplotlib.pyplot as plt
import numpy as np

# 랜덤 워크 생성 함수
def generate_random_walk(size):
    walk = np.zeros((size, size))
    x, y = size // 2, size // 2  # 중앙에서 시작

    for _ in range(size * size):
        walk[x, y] += 1
        direction = np.random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up' and x > 0:
            x -= 1
        elif direction == 'down' and x < size - 1:
            x += 1
        elif direction == 'left' and y > 0:
            y -= 1
        elif direction == 'right' and y < size - 1:
            y += 1

    return walk

# 4x4 랜덤 워크 데이터 생성
data_array = generate_random_walk(4)

# 컬러맵 그리기
plt.imshow(data_array, cmap='viridis', interpolation='none')

# 컬러바 추가
plt.colorbar()

# 제목 추가
plt.title('4x4 Random Walk Color Map')

# 그래프 보여주기
plt.show()