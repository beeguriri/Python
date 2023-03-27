import numpy as np

# 1차원 배열 생성
arr = np.array([1, 2, 3, 4, 5])

# 평균 계산
print(np.mean(arr))  # 3.0

# 중앙값 계산
print(np.median(arr))  # 3.0

# 표준편차 계산
print(np.std(arr))  # 1.4142135623730951

# 분산 계산
print(np.var(arr))  # 2.0

# 최대값, 최소값 계산
print(np.max(arr))  # 5
print(np.min(arr))  # 1

# 정규 분포
arr1 = np.random.normal(0, 1, size=10)
print(arr1)

# 균등 분포
arr2 = np.random.uniform(0, 1, size=10)
print(arr2)

# 이항 분포
# numpy.random.binomial(n, p, size)
# n: 베르누이 시행을 반복하는 횟수, p: 각 시행에서의 성공 확률, size는 생성할 난수의 개수
arr3 = np.random.binomial(10, 0.5, size=10)
print(arr3)

# 포아송 분포
# numpy.random.poisson(lam, size)
# lam: 단위 시간 또는 공간에서 발생하는 사건의 평균 개수, size: 생성할 난수의 개수
arr4 = np.random.poisson(3, 10)
print(arr4)
