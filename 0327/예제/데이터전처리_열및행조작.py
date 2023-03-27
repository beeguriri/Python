import pandas as pd
"""
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 추가 방법 1: 기존 열을 이용하여 새로운 열 추가
df['age2'] = df['age'] + 1

# 열 추가 방법 2: insert() 메소드를 이용하여 특정 위치에 열 추가
df.insert(loc=2, column='gender', value=['F', 'M', 'M', 'M', 'F'])

# 열 추가 방법 3: assign() 메소드를 이용하여 여러 개의 열 한 번에 추가
df = df.assign(age3=[26, 31, 36, 41, 46], height=[160, 170, 180, 175, 165])

# 출력
print(df)
"""
print("==============================")

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)
print(df)
print("==============================")

# 행 추가 방법 1: append() 메소드를 이용하여 단일 행 추가
new_row = {'name': 'Frank', 'age': 50, 'city': 'Seoul'}
df = df.append(new_row, ignore_index=True)
print(df)
print("==============================")

# 행 추가 방법 2: append() 메소드를 이용하여 여러 행 추가
new_rows = [{'name': 'George', 'age': 22, 'city': 'Toronto'},
            {'name': 'Helen', 'age': 27, 'city': 'Sydney'}]
df = df.append(new_rows, ignore_index=True)
print(df)
print("==============================")

"""
print("==============================")

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

print("==============================")

# 행 재정렬 방법 1: loc[]을 이용하여 행 순서 변경
df = df.loc[[4, 3, 2, 1, 0]]
print(df)

print("==============================")

# 행 재정렬 방법 2: sort_values() 메소드를 이용하여 열 기준으로 정렬
df = df.sort_values('age', ascending=True)  # ascending=False : 내림차순
print(df)

print("==============================")

# 열 재정렬 방법 1: 열 이름 순서 변경
df = df[['city', 'name', 'age']]
print(df)

print("==============================")

# 열 재정렬 방법 2: 열 이름을 알파벳 순서로 정렬
df = df.reindex(sorted(df.columns), axis=1)
print(df)

"""