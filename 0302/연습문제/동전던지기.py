# 동전 던지기
# 플레이어가 처음에 $50을 가지고 있다.
# 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다.
# 맞추면 $9을 따고 틀리면 $10을 잃는다.
# 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
# 동전을 던져서 나오는 수는 다음 문장을 이용하라.

import random

money = 50

while(money>=0 or money<=100):
    
    coin = random.randint(1,2)
    ans = int(input("(1)앞면 (2)뒷면 : "))
    
    if(coin==ans):
        money= money+9
        if money>100 :
            print("번돈이 $100 이상입니다.")
            break
        print(f"현재잔액 : {money}")
    else:
        money=money-10
        if money<0 :
            print("더이상 남은 돈이 없습니다.")
            break
        print(f"현재잔액 : {money}")
    
