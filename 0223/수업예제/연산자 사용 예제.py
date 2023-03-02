# 할당연산자 사용 예제
a = 10
b = 20
a += b  # a = a + b 와 동일
print(a)  # 30 출력
a -= b  # a = a - b 와 동일
print(a)  # 10 출력
a *= b  # a = a * b 와 동일
print(a)  # 200 출력
a /= b  # a = a / b 와 동일
print(a)  # 10.0 출력
a %= b  # a = a % b 와 동일
print(a)  # 10.0 출력

# 멤버쉽 연산자 사용 예제
a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print("W" in b)  # True 출력
print("k" not in b)  # True 출력

