import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 선 그래프 그리기
plt.plot(x, y1, label='sin')
plt.plot(x, y2, color='red', linestyle='--', linewidth=1, marker='+', markersize=1, label='cos')
# color: 그래프 색상
# linestyle: 선 스타일 (solid, dashed, dotted, dashdot 등)
# linewidth: 선 굵기
# marker: 마커 스타일 (circle, square, triangle 등)
# markersize: 마커 크기

# 그래프 타이틀과 축 라벨 설정
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')
# plt.legend(loc='best', fontsize=12, shadow=True, title='Legend')
# 범례를 사용하려면 각 그래프에 label이 반드시 있어야함
plt.legend(loc='best')

# 그래프 출력
plt.show()
