# 중첩for문

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

# 별문자 모양 그리기
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")	#print end의 기본은 개행문자 \n 들어가있음.
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
