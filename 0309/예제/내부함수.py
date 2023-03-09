# 내부함수 예제
def calculator():
    def add(a, b):
        return a + b    # 반환값으로 함수를 사용함

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    return add, subtract, multiply, divide

add, subtract, multiply, divide = calculator() # 함수를 변수에 할당 할 수 있음

print(add(10, 20))  # 출력결과: 30
print(subtract(10, 20))  # 출력결과: -10
print(multiply(10, 20))  # 출력결과: 200
print(divide(10, 20))  # 출력결과: 0.5

# 코드의 재사용성을 높일 수 있다
def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)  # 제곱 함수를 구현
cube = power(3)  # 세제곱 함수를 구현

print(square(3))  # 출력결과: 9
print(cube(3))  # 출력결과: 27
