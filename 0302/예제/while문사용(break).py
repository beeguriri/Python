# while문 사용 (break)

# 사용자로부터 값을 입력 받아,
# 입력한 값이 0이 아닌 동안 입력한 값들의 합을 출력하는 예제

sum = 0
while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break
    sum += num
print("입력한 값들의 합: ", sum)

# 사용자로부터 값을 입력 받아,
# 입력한 값 중에서 가장 큰 값을 출력하는 예제

max_value = 0
while True:
    num = int(input("숫자를 입력하세요: "))
    if num == 0:
        break
    if num > max_value:
        max_value = num
print("가장 큰 값: ", max_value)


