"""
Deposit 클래스를 생성하라.
이 클래스는 세 개의 인스턴스 변수 initial과 interest, n을 갖는다.
initial은 원금을 의미하고 interest는 년 이자율을 나타낸다.
초기화 함수에서 세 개의 인스턴스 변수를 전달 받은 값으로 설정해야 한다.
인스턴스 메소드 profit()은 n년 후 원리금을 반환한다.
n년 후 원리금은 initial * (1 + interest)n이다.
Deposit 클래스를 이용하여 100만원을 이율 3.5%로 7년간 저축했을 때 원리금을 구하는 프로그램을 작성하라.
단 원리금은 정수로 표시되어야 한다.
"""

class Deposit:

    # 생성자
    def __init__(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n

    def profit(self):
        return int(self.initial * ((1 + self.interest/100)**self.n))


dep = Deposit(1000000, 3.5, 7)
print(dep.profit())
