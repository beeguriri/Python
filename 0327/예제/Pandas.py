import pandas as pd

# 인덱스 자동생성
data = pd.Series([1, 2, 3, 4])
print(data)

# 인덱스 옵션지정
data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(data)

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)
print(s)

# 시리즈 인덱싱
print(s['a'])  # 10
print(s[['a', 'c', 'e']])  # a    10, c    30, e    50
print(s[:3])  # a    10, b    20, c    30
print(s[s > 30])  # d    40, e    50
