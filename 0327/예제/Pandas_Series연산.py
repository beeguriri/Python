import pandas as pd

# 시리즈 생성
data1 = {'a': 1, 'b': 2, 'c': 3}
data2 = {'a': 10, 'c': 30, 'd': 40}
s1 = pd.Series(data1)
s2 = pd.Series(data2)

# 덧셈 연산
s = s1 + s2
print(s)  # a    11.0, b     NaN, c    33.0, d     NaN            # dtype: float64

# 뺄셈 연산
s = s1 - s2
print(s)  # a    -9.0, b     NaN, c   -27.0, d     NaN           # dtype: float64

# 곱셈 연산
s = s1 * s2
print(s)  # a    10.0, b     NaN, c    90.0, d     NaN           # dtype: float64

# 나눗셈 연산
s = s1 / s2
print(s)  # a    0.1 , b     NaN, c    0.1 , d     NaN           # dtype: float64

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)
print(s)

# 집계 함수 예시
print(s.sum())  # 150
print(s.mean())  # 30.0
print(s.std())  # 15.811388300841896
print(s.max())  # 50
print(s.min())  # 10
