# 리스트 컴프리헨션
# [표현식 for 항목 in 반복가능객체 if 조건문]
# for 반복문을 통해서 생성된 항목이 조건문을 통과했을때 표현식에 반영

# 1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)

# 리스트 내 모든 요소에 1을 더하는 예제
original_list = [1, 2, 3, 4, 5]
new_list = [num + 1 for num in original_list]
print(new_list)

# 리스트 내 문자열의 길이를 구하는 예제
words = ['apple', 'banana', 'cherry', 'durian']
word_lengths = [len(word) for word in words]
print(word_lengths)  

# 문자열 리스트에서 길이가 6 이상인 문자열만 대문자로 바꾸기
words = ["apple", "banana", "orange", "grape", "watermelon"]
result = [word.upper() for word in words if len(word) >= 6]
print(result)  

# 리스트 내 중첩된 요소들을 단일 리스트로 만드는 예제
original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [num for sublist in original_list for num in sublist]
# original_list를 순회하며 sublist를 만들고, 
# 그 sublist를 다시 순회하며 num을 뽑아서 제일 앞의 num에 넣어줌
print(new_list)

# 주어진 이차원 리스트에서 짝수만 리스트로 생성하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]

# 리스트 인덱싱
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])  # [1, 2, 3] 출력
print(matrix[1])  # [4, 5, 6] 출력
print(matrix[2])  # [7, 8, 9] 출력
print(matrix[0][1])  # 2 출력
print(matrix[1][2])  # 6 출력


# 리스트 요소 수정, 추가, 제거하기
# 리스트 추가
# append(element) :리스트의 끝에 새로운 요소를 추가
# insert(index, element) : 리스트의 원하는 위치에 요소를 추가

# 리스트 삭제
# 슬라이싱을 이용
my_list = [1, 2, 3, 4, 5]
my_list[1:4] = []
print(my_list) # 출력 결과: [1, 5]
#del 키워드 이용
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list) # 출력 결과: [1, 2, 4]
# remove(element) 메서드 :리스트에서 특정 요소를 찾아 제거
# pop(index) 메서드 : 인덱스를 지정하여 특정 위치의 요소를 제거, 별도 지정안하면 마지막 요소 제거
# clear() 메서드 : 리스트의 모든 요소 제거


# 리스트 내장함수
# sum(list_name) / max(list_name) / min(list_name)
# sorted(list_name) : 오름차순 / reversed(list_name) : 내림차순 => 새로운 배열 반환
# list_name.sort() / list_name.reverse() => 원본정렬

