# 500만원을 년이율 5%로 복리 저금했을 때 5년 후의 원리금의 합계를 출력하는 프로그램
# 원리금 =  P x (1 + r)^t
# P 는 최초 투자 금액, r 은 연이자율, t 는 투자 기간(년)
# 500만원, 년5%, 5년후 => 6,381,408

i_money = int(input("원금을 입력하세요."))
i_per = float(input("연이율(%)를 입력하세요."))
i_year = int(input("기간을 입력하세요."))

total = i_money * (1+ i_per/100)**i_year  #total을 int형으로 지정하면, 소수점 이하 버림

print(f"원금{i_money:,d}원, 연이율{i_per}%의 {i_year}년 후 원리금의 합계는 {total:,.0f}원 입니다.")
