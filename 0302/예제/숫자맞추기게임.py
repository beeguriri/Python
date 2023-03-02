# 숫자 맞추기 게임

import random

# 1부터 100 사이의 임의의 수를 선택합니다

secret_number = random.randint(1, 100)

while True:
    # 사용자가 숫자를 입력합니다
    guess = int(input("Guess the secret number (between 1 and 100): "))

    # 입력한 숫자와 비교합니다
    if guess < secret_number:
        print("Up")
    elif guess > secret_number:
        print("Down")
    else:
        print("Correct!")
        break  # 정답을 맞췄으므로 반복문을 종료합니다
