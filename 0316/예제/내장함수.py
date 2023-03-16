# bin(x), oct(x), hex(x) : 10진 정수 x에 대한 2진수, 8진수, 16진수 문자열 반환
# int(str, base=10) <- base를 바꿔주면 해당 진수의 값으로 출력
print(bin(12))          #'0b1100'
print(int('123'))       #123
print(int('1010', 2))   #10

# enumerate(iterable,start=0)
# 주로 순서가 있는 자료형(리스트, 튜플 등)의 각 요소에 대해 인덱스와 값을 동시에 반환하는데 사용됩니다.
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)

# eval(expr,[globals[,locals]])
# 문자열로 표시된 파이썬 코드를 실행하고 결과를 반환
result = eval('2 + 3 * 4')
print(result)  # 출력 결과: 14

# filter(func,seq)
# 시퀀스의 각 요소에 대해 함수를 적용하여 결과가 True인 것만 모아서 리스트로 반환하는 함수
# 리스트에서 짝수만 추출하는 예시
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력 결과: [2, 4, 6, 8, 10]

# map(함수, 시퀀스)
# 시퀀스의 각 원소에 대해 지정된 함수를 적용하여, 새로운 리스트를 반환
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # 출력결과: [1, 4, 9, 16, 25]

# ord(ch)
# ch에 대한 ASCII 코드 반환
print(ord('A')) #65

#repr(obj)
# obj를 문자열로 변환
print(repr(b'0011')) # b'0011'
my_list = [1, 2, 3]
list_str = repr(my_list)
print(list_str)  # [1, 2, 3]

# round(x, n=0)
# 실수 x를 소수점 아래 n자리로 반올림하여 반환

#zip(seq, *seqs)
#seq 요소와 *seqs 요소의 튜플 쌍으로 이루어진 리스트 iterable 반환
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 32, 28]

for name, age in zip(names, ages):
    print(name, age)

