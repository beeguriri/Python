# 기존 함수 정의 방법
def add(a, b):
    return a + b

# 람다 함수 정의 방법
lambda_add = lambda a, b: a + b

# 함수 호출
print(add(3, 4))             # 7
print(lambda_add(3, 4))      # 7

students = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 70},
]

# 점수(score)를 기준으로 학생 리스트 정렬
sorted_students = sorted(students, key=lambda student: student['score'], reverse=True)
print(sorted_students)
# 출력 결과: [{'name': 'Bob', 'score': 90}, {'name': 'Alice', 'score': 80}, {'name': 'Charlie', 'score': 70}]

# 함수의 반환값으로 사용
def get_operator(operator):
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '-':
        return lambda a, b: a - b
    elif operator == '*':
        return lambda a, b: a * b
    elif operator == '/':
        return lambda a, b: a / b

# 함수의 반환값이 람다함수
add_func = get_operator('+')
result1 = add_func(3, 4)  # 7

multiply_func = get_operator('*')
result2 = multiply_func(3, 4)  # 12

