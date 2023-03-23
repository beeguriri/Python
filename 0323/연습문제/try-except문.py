"""
 사용자로부터 문자열을 입력 받는다
문자열이 data의 key와 같으면 value를 출력하고 다시 문자열을 입력 받는다
문자열 에 해당하는 key가 없으면 "항목이 없습니다"라는 메시지를 출력하고 종료한다.
"""
data = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6}

# try-except문 사용해서 구현
while True:
    try:
        inputD = input("요일을 입력하세요 : ")
        value = data[inputD.title()]
        print(value)
    except KeyError:
        print("항목이 없습니다.")
        break

# try-except문 쓰지않고 구현
while True:
    inputD = input("요일을 입력하세요 : ")
    value = data.get(inputD.title(), None)
    if value is not None:
        print(value)
    else:
        print("항목이 없습니다.")
        break
