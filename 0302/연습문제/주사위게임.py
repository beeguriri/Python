# 주사위 게임
# 두 주사위를 던졌을 때, 합이 7이 되면 이김,
# 그렇지 않으면 지는 간단한 주사위 게임을 만들어보세요.

import random

while True:
    
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)

    if (r1+r2)==7:
        print("이겼습니다.")
        break
    else:
        print("다시 던집니다.")
            
    
