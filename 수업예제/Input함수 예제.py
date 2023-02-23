# input() 함수를 이용하여 사용자로부터 입력받아 계산하기
# int형으로 변환해주지않으면 문자열로 인식함
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division:.2f}")


# input(), 포매팅, 산술식을 이용하여 계산하기
#"""...""" : 여러행 문자열
result = f"""
입력한 숫자:
첫 번째 숫자: {num1}
두 번째 숫자: {num2}

산술 연산 결과:
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} * {num2} = {num1 * num2}
{num1} / {num2} = {num1 / num2:.2f}
"""

print(result)
