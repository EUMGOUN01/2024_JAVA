import matplotlib.pyplot as plt
import seaborn as sns

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

sns.set_style('whitegrid')  # seaborn 스타일 설정
plt.plot(input_values, squares, linewidth=3)

# 그래프 타이틀과 축 라벨 설정
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 눈금 레이블 크기 설정
plt.tick_params(axis='both', labelsize=14)

plt.show()