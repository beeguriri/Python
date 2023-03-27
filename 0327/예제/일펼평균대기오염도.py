import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('일별평균대기오염도_2022.csv', encoding="euc-kr")

# 데이터프레임 정보 확인
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())  # 결측치 개수 출력

mise = df.iloc[0:20, [0, 1, 6, 7]]
print(mise)

# 조건 사용하기
# 행을 선택 후 가지고 올 열 선택
# 다중조건
sub_df = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 100) & (df['초미세먼지농도(㎍/㎥)'] >= 100)].iloc[:, [0, 1, 6, 7]]
print("sub_df")
print(sub_df)

# 단일조건
sub_df2 = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 200)].iloc[:, [0, 1, 6]]
# sub_df2 = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 200)].loc[:, ['측정일시', '측정소명', '미세먼지농도(㎍/㎥)']]
print("sub_df2")
print(sub_df2)

# 행과 열을 동시에 지정
sub_df3 = df.loc[df['미세먼지농도(㎍/㎥)'] >= 300, ['측정일시', '측정소명', '미세먼지농도(㎍/㎥)']]
print("sub_df3")
print(sub_df3)
print(sub_df3.loc[:, '미세먼지농도(㎍/㎥)'].mean())
print(sub_df3.loc[:, '미세먼지농도(㎍/㎥)'].max())

# 결측치 제거
print(sub_df3.isnull())  # 결측치 여부 확인 : True -> 결측치
dropped_df = sub_df3.dropna()  # 결측치 제거
print(dropped_df)

# 중복 확인
print(sub_df3.duplicated())

# 중복 제거
deduplicated_df = sub_df3.drop_duplicates()
print(deduplicated_df)
print("=======================")

# 날짜형식 데이터 변환
df['date'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')
print(df.head(100))

df_year = df.groupby('측정소명').resample('AS', on='date').mean(numeric_only=True)
print(df_year)

df_month = df.groupby('측정소명').resample('M', on='date').mean(numeric_only=True)
print(df_month)

df_day = df.groupby('측정소명').resample('D', on='date').mean(numeric_only=True)
print(df_day)

print("=======================")
# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

print(df.head(20))

print("=======================")
# 월별 미세먼지와 초미세먼지 농도 평균 계산
df_monthly = df.resample('M', on='측정일시').mean(numeric_only=True)

# 그래프 그리기
plt.plot(df_monthly.index.month, df_monthly['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_monthly.index.month, df_monthly['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()

# 지역별 미세먼지와 초미세먼지 농도 평균 계산
df_area = df.groupby('측정소명').mean(numeric_only=True).head(10)

# 그래프 그리기
plt.bar(df_area.index, df_area['미세먼지농도(㎍/㎥)'], label='PM10')
plt.bar(df_area.index, df_area['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Area')
plt.ylabel('Concentration')
plt.title('Air Pollution by Area')
plt.show()

# 그래프 그리기
plt.boxplot([df['미세먼지농도(㎍/㎥)'], df['초미세먼지농도(㎍/㎥)']])
plt.xticks([1,2],['PM10', 'PM2.5'])
plt.ylabel('Concentration')
plt.title('Air Pollution Boxplot')
plt.show()

# 이상치를 모아서 result.csv 파일로 저장
q1_pm10 = df['미세먼지농도(㎍/㎥)'].quantile(0.25)
q3_pm10 = df['미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr_pm10 = q3_pm10 - q1_pm10
q1_pm25 = df['초미세먼지농도(㎍/㎥)'].quantile(0.25)
q3_pm25 = df['초미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr_pm25 = q3_pm25 - q1_pm25

outlier_df = df[((df['미세먼지농도(㎍/㎥)'] < q1_pm10 - 1.5 * iqr_pm10) | (df['미세먼지농도(㎍/㎥)'] > q3_pm10 + 1.5 * iqr_pm10))
                &
                ((df['초미세먼지농도(㎍/㎥)'] < q1_pm25 - 1.5 * iqr_pm25) | (df['초미세먼지농도(㎍/㎥)'] > q3_pm25 + 1.5 * iqr_pm25))]

outlier_df.to_csv('result.csv', index=False, encoding='utf-8-sig')
