import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
#print(data)

df = pd.DataFrame(data)
#print(df)

# 데이터프레임 정보 출력
print(df.head(2))            # 기본 : 상위 5개 데이터 출력, 숫자입력 시 해당 개수만큼 출력
print(df.tail(2))            # 기본 : 하위 5개 데이터 출력, 숫자입력 시 해당 개수만큼 출력
print(df.info())            # 데이터프레임 정보 출력
print(df.describe())        # 수치형 열의 기술 통계 정보 출력(평균, 표준편차, 분위 ...)
print(df.columns)           # 열 이름 출력 Index(['name', 'age', 'city'], dtype='object')
print(df.index)             # 행 인덱스 출력 RangeIndex(start=0, stop=5, step=1)
print(df.dtypes)            # 열의 데이터 타입 출력
print(df.shape)             # 데이터프레임의 크기 출력 (5, 3)
print(df.isnull().sum())    # 결측치 개수 출력
