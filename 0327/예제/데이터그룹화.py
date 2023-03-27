# 데이터 그룹화
# 데이터를 특정 기준에 따라 그룹화하고 집계

import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 30, 35, 40, 45, 50],
        'score1': [80, 70, 85, 75, 90, 95],
        'score2': [85, 75, 90, 80, 95, 100]}

df = pd.DataFrame(data)
print(df)
# count
print("====count====")
print(df.groupby('gender')[['score1', 'score2']].count())

# size
print("====size====")
print(df.groupby('gender')[['score1', 'score2']].size())

# sum
print("====sum====")
print(df.groupby('gender')[['score1', 'score2']].sum())

# mean
print("====mean====")
print(df.groupby('gender')[['score1', 'score2']].mean())

# median
print("====median====")
print(df.groupby('gender')[['score1', 'score2']].median())

# min
print("====min====")
print(df.groupby('gender')[['score1', 'score2']].min())

# max
print("====max====")
print(df.groupby('gender')[['score1', 'score2']].max())

# std
print("====std====")
print(df.groupby('gender')[['score1', 'score2']].std())

# var
print("====var====")
print(df.groupby('gender')[['score1', 'score2']].var())

# sem
print("====sem====")
print(df.groupby('gender')[['score1', 'score2']].sem())

# describe
print("====describe====")
print(df.groupby('gender')[['score1', 'score2']].describe())

print("=========================")
# 데이터프레임 생성
data = {'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'age': [20, 30, 25, 35, 27],
        'city': ['Seoul', 'Busan', 'Seoul', 'Incheon', 'Seoul']}

df = pd.DataFrame(data)
print(df.groupby('city')[['age']].mean())


print("=========================")
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': [1, 2, 3, 4, 5, 6, 7, 8],
    'D': [10, 20, 30, 40, 50, 60, 70, 80]
})

result = df.groupby(['A', 'B']).agg({'C': 'count', 'D': ['sum', 'mean']})
print(result)
