# 딕셔너리 생성
fruits = {'apple': 3, 'banana': 2, 'orange': 1}

# keys 함수를 사용하여 딕셔너리의 키를 리스트로 변환
keys_list = list(fruits.keys())
print(keys_list)  # ['apple', 'banana', 'orange']

# values 함수를 사용하여 딕셔너리의 값을 리스트로 변환
values_list = list(fruits.values())
print(values_list)  # [3, 2, 1]

# items 함수를 사용하여 딕셔너리의 (키, 값) 쌍을 리스트로 변환
items_list = list(fruits.items())
print(items_list)  # [('apple', 3), ('banana', 2), ('orange', 1)]

# 딕셔너리 생성
fruits = {'apple': 3, 'banana': 2, 'orange': 1}

# get 함수를 사용하여 딕셔너리에서 특정 키에 해당하는 값을 가져옴
print(fruits.get('apple'))  # 3
print(fruits.get('grape'))  # None

# setdefault 함수를 사용하여 딕셔너리에 새로운 (키, 값) 쌍 추가
fruits.setdefault('grape', 5)
print(fruits)  # {'apple': 3, 'banana': 2, 'orange': 1, 'grape': 5}

# pop 함수를 사용하여 딕셔너리에서 특정 키의 (키, 값) 쌍 제거하고 값을 반환
grape_count = fruits.pop('grape')
print(grape_count)  # 5
print(fruits)  # {'apple': 3, 'banana': 2, 'orange': 1}

# update 함수를 사용하여 딕셔너리에 다른 딕셔너리의 (키, 값) 쌍 추가 또는 업데이트
new_fruits = {'pear': 2, 'apple': 5}
fruits.update(new_fruits)
print(fruits)  # {'apple': 5, 'banana': 2, 'orange': 1, 'pear': 2}

