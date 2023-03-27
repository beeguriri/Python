import pandas as pd

# 매출 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'],
        'Age': [20, 30, 40, 50, 30, 40, 50, 60],
        'Time': ['Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon'],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)

# 피벗테이블 생성
result = pd.pivot_table(df, index='Region', columns='Time', values='Sales', aggfunc='sum')
print(result)

print("=========================")
# cut : 주어진 데이터를 일정한 구간으로 나누어 범주형 데이터로 변환하는 함수
result2 = pd.pivot_table(df, index='Region', columns=pd.cut(df['Age'], [10, 30, 50, 70]),
                         values='Sales', aggfunc='count')
print(result2)
