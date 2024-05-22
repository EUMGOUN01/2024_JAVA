import matplotlib.pyplot as plt
import numpy as np

data = [
    [1, 1, 0, 1],
    [-1, 1, 1, 0],
    [0, 0, -1, 0],
    [1, -1, 0, -1]
]

# 데이터 배열을 numpy 배열로 변환
data_array = np.array(data)

# 컬러맵 그리기
plt.imshow(data_array, cmap='viridis', interpolation='none')

# 컬러바 추가
plt.colorbar()

# 제목 추가
plt.title('4x4 컬러 맵')

# 그래프 보여주기
plt.show()