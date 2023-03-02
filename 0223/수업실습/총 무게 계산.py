#판매자가 딸기와 포도를 판매하고 있다.
#포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 113.5g이다.
#사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아 총 무게를 계산하여 출력하는 프로그램을 작성하고 실행하라.

grape = int(input("포도의 개수"))
straw =  int(input("딸기의 개수"))

total = float (grape * 75 + straw * 113.5)

print(f"포도 {grape}알과 딸기 {straw}알의 무게는 {total:.1f}g 입니다.")