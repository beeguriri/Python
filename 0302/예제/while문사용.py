# while문 사용

# 1~10까지 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    
# 1에서부터 10까지의 짝수를 출력하는 예제
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# 1에서부터 100까지의 합을 출력하는 예제
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
