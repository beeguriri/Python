import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

url = 'http://www.yes24.com/24/Category/BestSeller'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)

#제목
title = soup.select('li.num1')[0].select('p')[2].select_one('a').text
print(title)

#저자
author = soup.select('li.num1')[0].select('p.aupu')[0].select('a')[0].text
print(author)

#출판사
publisher = soup.select('li.num1')[0].select('p.aupu')[0].select('a')[-1].text
print(publisher)

#price
price = soup.select('li.num1')[0].select_one('p.price').select_one('strong').text
print(price)

books = []
for i in range(1, 10):
    rank = i
    title = soup.select(f'li.num{i}')[0].select('p')[2].select_one('a').text
    author = soup.select(f'li.num{i}')[0].select('p.aupu')[0].select('a')[0].text
    publisher = soup.select(f'li.num{i}')[0].select('p.aupu')[0].select('a')[-1].text
    price = soup.select(f'li.num{i}')[0].select_one('p.price').select_one('strong').text[:-1].replace(',', '') #원은 빼고 가져오기
    books.append([rank, title, author, publisher, price])
print(books)

# csv파일 내보내기
df = pd.DataFrame(books, columns=['순위', '책제목', '저자', '출판사', '가격'])
df.to_csv('books_info.csv', index=False, encoding='euc-kr')

# 그래프 그리기
df = pd.read_csv('books_info.csv', encoding='euc-kr')
x = df['책제목'].str[0:8]
print(df.info())
y = df['가격']

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
plt.bar(x, y)
plt.title('베스트셀러 가격')
plt.xlabel('책제목')
plt.ylabel('가격')
plt.xticks(fontsize=5)
plt.yticks([0, 5000, 10000, 15000, 20000, 25000])
plt.show()
