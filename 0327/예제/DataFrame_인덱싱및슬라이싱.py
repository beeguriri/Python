import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

print("열 선택방법")
# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name']  # name의 열에 있는 모든 행의 값
# ":" => 모든 행 가져옴 (1:2 => 1,2행 가져옴)
print(name_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1, 2]]  # 위치인덱스로 가져옴
print(name_age_col)

print("행 선택방법")
# 행 선택 방법 1: 대괄호([])를 이용한 단일 행 선택
row_0 = df.iloc[0]
print(row_0)

# 행 선택 방법 2: loc[]를 이용한 단일 행 선택
row_1 = df.loc[1]
print(row_1)

# 행 선택 방법 3: iloc[]를 이용한 복수 행 선택
rows_1_3 = df.iloc[[1, 3]]
print(rows_1_3)

# 행 선택 방법 4: loc[]를 이용한 복수 행 선택
rows_2_4 = df.loc[[2, 4]]
print(rows_2_4)

sub_df = df.loc[df['age'] >= 30]
print(sub_df)

# 행 선택 방법 5: 슬라이싱을 이용한 범위 지정
rows_1_3 = df[1:4]
print(rows_1_3)

# 행 선택 방법 6: query()를 이용한 조건에 따른 행 선택
rows_age_over_30 = df.query('age > 30')
print(rows_age_over_30)

# 나이가 30 이상이고, 도시가 'London'인 데이터 선택
sub_df = df.query('age >= 40 and city == "London" or city=="Tokyo"')
print(sub_df)
