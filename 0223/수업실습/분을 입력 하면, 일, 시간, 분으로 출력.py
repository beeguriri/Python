# 분(min)을 입력 하면, 일, 시간, 분으로 출력하는 프로그램
# 예 : 1550분은 1일 1시간 50분

input_min = int(input("분을 입력하세요."))

hour = input_min // 60
min = input_min % 60
day = 0

if hour >=24:
    day = hour // 24
    hour = hour - day*24
    
print(f"{input_min}분은 {day}일 {hour}시간 {min}분 입니다.")
        
