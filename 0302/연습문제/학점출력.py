#사용자로부터 이수한 학점을 입력 받는다.
#학점이 40학점 미만이면 "1학년입니다"를 출력하고,
#40이상 80미만이면 "2학년입니다"를 출력한다.
#학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.

score = int(input("이수한 학점을 입력하세요 : "))

if score >=80:
    print("졸업반입니다.")
elif score >=40:
    print("2학년입니다.")
else:
    print("1학년입니다.")
