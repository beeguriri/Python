# 사용자로부터 숫자를 입력받아, 홀수인지 짝수인지 판별하기
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")
