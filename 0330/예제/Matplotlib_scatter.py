import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
# x, y의 갯수가 똑같아야함!
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
plt.scatter(x, y)
plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)
# color: 마커 색상
# marker: 마커 스타일 (circle, square, triangle 등)
# s: 마커 크기
# alpha: 마커 투명도

# 그래프 타이틀과 축 라벨 설정
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right', fontsize=12, shadow=True, title='Legend')

# 그래프 출력
plt.show()
