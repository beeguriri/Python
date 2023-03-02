# 사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
# 또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다.
# 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.
# new hour : 1 pm

hour = int(input("현재 시간을 입력하세요(1~12) : "))
ampm = int(input("(1)am / (2)pm : "))
ahead = int(input("경과시간을 입력하세요 : "))

newhour = hour+(ahead%24)

if ampm == 1:
    if newhour <= 12:
        print("최종시간 : ", newhour, "am")
    else:
        print("최종시간 : ", newhour-12, "pm")
else:
    if newhour <= 12:
        print("최종시간 : ", newhour, "pm")
    else:
        print("최종시간 : ", newhour-12, "am")    
