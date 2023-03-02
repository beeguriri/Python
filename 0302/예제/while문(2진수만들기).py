# while문(2진수 만들기)

num = int(input("10진수를 입력하세요: "))
binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary		# 기존의 문자열 앞에 추가
    num = num // 2					# //: 몫 구하기

print("입력한 수의 2진수 표현: ", binary)
