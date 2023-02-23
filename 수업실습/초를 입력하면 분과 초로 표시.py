# 초를 입력하면 분과 초로 표시하는 프로그램.
# 예를 들어, 200초를 입력하면 3분 20초로 표현하라

input_sec = int(input("초를 입력하세요."))

min = input_sec // 60 #몫
sec = input_sec % 60 #나머지

print(f"{input_sec}는 {min}분 {sec}초 입니다.")
