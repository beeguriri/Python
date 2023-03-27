# DataFrame
# 2차원 테이블 형태의 자료구조
# 인덱스와 열(column)로 구성된 데이터

import pandas as pd
import numpy as np

# 데이터프레임 생성 방법 1: 딕셔너리를 이용한 데이터프레임 생성
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df1)

# 데이터프레임 생성 방법 2: 리스트를 이용한 데이터프레임 생성
data = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
df2 = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df2)

# 데이터프레임 생성 방법 3: Numpy 배열을 이용한 데이터프레임 생성
arr = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df3)

# 데이터프레임 생성 방법 4: 시리즈를 이용한 데이터프레임 생성
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s3 = pd.Series([7, 8, 9])
df4 = pd.DataFrame({'A': s1, 'B': s2, 'C': s3})
print(df4)

# 데이터프레임 생성 방법 5: 외부 데이터 파일을 이용한 데이터프레임 생성
df5 = pd.read_csv('data.csv')
print(df5)

