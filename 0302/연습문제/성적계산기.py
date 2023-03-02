# 성적 계산기
# 사용자로부터 국어, 영어, 수학 세 과목의 성적을 입력받아,
# 각 과목의 평균 점수와 총 평균 점수를 계산한 후, 학점을 출력하는 프로그램을 작성하세요.
# 평균 점수는 소수점 둘째자리까지 출력합니다.
# 총 평균 점수는 국어: 40%, 영어: 40%, 수학: 20%로 가중치를 부여하여 계산합니다.
# 총 평균 점수가 90점 이상인 경우 "A", 80점 이상인 경우 "B", 70점 이상인 경우 "C", 60점 이상인 경우 "D", 60점 미만인 경우 "F"를 출력합니다.

print("[성적 계산기]")
ko = int(input("국어 점수를 입력하세요: "))
en = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))

print("\n[성적 결과]")
avgko = ko
avgen = en
avgmath = math
avgtotal = (ko*0.4 + en*0.4 + math * 0.2)
print(f"각 과목의 평균 점수 : {avgtotal:.2f}")

grade = "A" if avgtotal >= 90 else ("B" if avgtotal >= 80 else ("C" if avgtotal >= 70 else ("D" if avgtotal >= 60 else "F")))
print("학점 : ", grade)