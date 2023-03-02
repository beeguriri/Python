# random() : 0.0 ~ 1.0 사이의 실수 난수 생성
# randint(a,b) : a이상 b이하의 정수 난수 생성

import random

# 1부터 100 사이의 정수 중 하나를 무작위로 생성
random_number = random.randint(1, 100)
print(random_number)

# 리스트 fruits에서 무작위로 선택된 하나의 과일을 출력
fruits = ['apple', 'banana', 'orange', 'pear']
print(random.choice(fruits))

# 리스트 x의 항목을 무작위로 섞기
cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
random.shuffle(cards)
print(cards)
# 출력 예시: ['Q', '5', '10', '7', '4', 'K', '2', 'A', 'J', '9', '3', '6', '8']


# 도시와 날씨 리스트 정의
cities = ['서울', '부산', '인천', '대구', '광주', '대전']
weathers = ['맑음', '흐림', '비', '눈', '우박']

# 도시와 날씨를 무작위로 선택하여 출력
city = random.choice(cities)
weather = random.choice(weathers)
print(f'{city}의 날씨는 {weather}입니다.')
