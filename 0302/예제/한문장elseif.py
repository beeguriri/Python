# 한 문장 else-if문
num = int(input("숫자를 입력하세요: "))
result = "10보다 큽니다" if num > 10 else "10보다 작거나 같습니다"
print(result)


# 한 문장 else-if문 중첩
score = int(input("성적을 입력하세요: "))
grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else ("D" if score >= 60 else "F")))
print(grade)


# 세 개의 수 중 가장 작은 수를 출력하는 프로그램
a = 10
b = 20
c = 5
min_value = a if a < b and a < c else (b if b < c else c)
print("가장 작은 수는", min_value, "입니다.")
