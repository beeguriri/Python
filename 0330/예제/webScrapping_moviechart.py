import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# 첫번째 태그 하나 가지고 나옴
# html 구조 확인 -> ol태그 하나에 li태그가 여러개 달려있는 구조
ol = soup.select_one('.list_movieranking')
# print(ol)

# ol태그 안의 li태그를 모두 찾아옴
# find_all : list 형태로 저장
li_list = ol.find_all('li')
# print(li_list)

# li태그 내의 내용 저장
movie = []
for li in li_list:
    rank = li.select_one('.rank_num').text
    name = li.select_one('.link_txt').text
    age = li.select_one('.ico_see').text
    grade = li.select_one('.txt_grade').text
    num = li.select_one('.txt_num').text[:-1]  # '%'바로 앞까지 가지고오기
    mvdate = li.select_one('.txt_info > .txt_num').text  # num과 클래스명 중복이므로 txt_info 하위의 txt_num 클래스 가져옴
    # print(rank, name, age, grade, num, mvdate)
    movie.append([rank, name, age, grade, num, mvdate])

# print(movie)

# 판다스 이용해서 csv파일로 저장
import pandas as pd

# list를 dataframe으로 변환 후 csv 파일로 저장
df = pd.DataFrame(movie, columns=['순위', '영화명', '관람가', '평점', '예매율', '개봉일'])
df.to_csv('movie_info.csv', index=False, encoding='euc-kr')

# 데이터 분석
# 파일을 읽어오면 숫자형 데이터는 자동으로 변환해줌
df = pd.read_csv('movie_info.csv', encoding='euc-kr')
print(df.info())  # data type 확인
print(df[df['평점'] >= 8])

# 그래프 그리기
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # 한글이 있는 데이터는 폰트설정 필요

# 개봉일 날짜 전처리
df['개봉일'] = pd.to_datetime(df['개봉일'], format='%y.%m.%d')
print(df.info())  # 형변환 잘되었는지 반드시 확인

df_weekly = df.resample('W', on='개봉일').mean(numeric_only=True)  # 주의 마지막날 기준으로 주단위 리샘플링
print(df_weekly)  # NAN 확인 -> 결측치 처리
df_weekly = df_weekly.fillna(0)  # 결측치 대체
# df_weekly = df_weekly.dropna()  # 결측치 제거
print(df_weekly)

plt.plot(df_weekly.index, df_weekly['예매율'])
plt.show()
