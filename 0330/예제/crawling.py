import requests
from bs4 import BeautifulSoup

url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("h4", class_="article-title")
for title in titles:
    print(title.text.strip())  # .strip 양쪽 끝 공백 제거
    print(title.get('class'))

# .get : 태그의 속성 반환 (href 주소, 클래스명...)
# .text : 태그가 가지고 있는 텍스트 가지고 나옴


# 다른방법
#div_menu = soup.find('div', {'class': 'list'})
div_menu = soup.find_all('div', class_='list')
print(div_menu)
#links = div_menu.find_all('a')
links = []
for div in div_menu:
    links = div.get('a')
print(links)

# for link in links:
#     print("get", link.get('href'))
#     print("text", link.text)
