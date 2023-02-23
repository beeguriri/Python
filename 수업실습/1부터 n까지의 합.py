#1부터 100까지의 합을 구하여 출력하는 프로그램을 작성하고 실행하라.
#1부터 n까지의 합은 n(n+1)/2로 주어진다.

num = int(input("정수를 입력하세요."))

result = int(num * (num + 1) / 2)

print(f"1부터 {num}까지의 합은 {result} 입니다.")

#a부터 b까지의 합
#sum = n(a+b)/2

numa = int(input("정수1을 입력하세요."))
numb = int(input("정수2을 입력하세요."))

n =numb-numa + 1
sum = int (n * (numa + numb) / 2)

print(f"{numa}부터 {numb}까지의 합은 {sum} 입니다.")