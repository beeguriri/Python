import pandas as pd

# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5'],
        'bool_col': [True, False, True, False, True],
        'category_col': ['a', 'b', 'c', 'a', 'b'],
        'date_col': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']}

df = pd.DataFrame(data)
print(df.dtypes)

# 열 데이터 형 변환
df['int_col'] = df['int_col'].astype(float)  # 정수형 -> 실수형
df['float_col'] = df['float_col'].astype(int)  # 실수형 -> 정수형
df['str_col'] = df['str_col'].astype(bool)  # 문자열 -> 불리언형
df['bool_col'] = df['bool_col'].astype(str)  # 불리언형 -> 문자열형
df['category_col'] = df['category_col'].astype('category')  # 문자열 -> 범주형 (그룹화 할 때 사용)
df['date_col'] = pd.to_datetime(df['date_col'])  # 문자열 -> 날짜/시간형

# 데이터프레임 정보 출력
print(df.dtypes)

print("=========================================")

# 데이터프레임 생성
data = {'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'age': [20, 30, 25, 35, 27],
        'city': ['Seoul', 'Busan', 'Seoul', 'Incheon', 'Seoul']}

df = pd.DataFrame(data)

# gender 열을 category 형으로 변환
df['gender'] = df['gender'].astype('category')

# city 열을 category 형으로 변환
df['city'] = df['city'].astype('category')

# 카테고리별 데이터 개수 확인
print(df['gender'].value_counts())
print(df['city'].value_counts())

# 카테고리별 통계량 확인
print(df.groupby('gender').mean(numeric_only=True))
print(df.groupby('city').mean(numeric_only=True))

print("=========================================")

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie'],  # object
        'age': ['25', '30', '35'],  # object
        'score1': [80, 70, 85],  # int
        'score2': [85, 75, 90]}  # int

df = pd.DataFrame(data)
print(df.info())

# apply() 메소드를 이용하여 모든 문자열 값을 대문자로 변환
df['name'] = df['name'].apply(lambda x: x.upper())
df['age'] = df['age'].apply(int)  # 문자열 -> 정수형으로 변경

print(df)
print(df.info())
