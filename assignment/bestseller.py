import requests
from bs4 import BeautifulSoup

url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=YearlyBest&BranchType=1&CID=0&Year=2022'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
print("#################################")

lists = soup.find_all('div', {'class': 'ss_book_list'})
print(lists)

book = []
book = lists[0].find_all('li')

for list in lists:
    name = list.find('b')
    print(name)


# for li in list:
#     #name = li.find('a', {'class': 'bo3'}).find('b').text
#     name.append(li.find('b'))



#ss_book_box
