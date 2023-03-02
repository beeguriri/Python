# for문사용 (range)

#range(start, stop, step)
#start 생략 시 : 0
#step 생략 시 : 1

for i in range(1, 11): #1이상, 11미만
    print(i)

#1이상 11미만, 짝수만 출력
for i in range(2, 11, 2):	
    print(i)

#1이상 11미만, 홀수만 출력
for i in range(1, 11, 2):	
    print(i)
    
#10부터 1까지 거꾸로 출력하기
for i in range(10, 0, -1):
    print(i)

# 0에서 4까지의 정수 시퀀스 생성
for i in range(5):	#start, step 생략
    print(i)


