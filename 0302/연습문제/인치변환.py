# 사용자로부터 cm 단위의 길이를 입력 받는다.
# 입력 값이 음수이면 "잘못 입력하였습니다"라는 메시지를 출력하고
# 양수이면 길이를 인치로 변환하여 출력하는 프로그램을 작성하라.
# 1인치 = 2.54cm

cm = int(input("길이를 입력하세요(cm): "))

if cm >=0:
    inch = cm*2.54
    print("인치로 변환 :", inch, "inch")
else: print("잘못 입력하였습니다.")    
