#두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성
def box(n,m):
    i=0
    while i<n:
        print('*'*m)
        i=i+1

box(2,4)    #print(box(2,4) : 결과 None

# 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성
# 예: 123 -> 1+2+3 = 6

def sumnum(n):
    for char in str(n):
        sumnum += int(char)
    return sumnum

print(sumnum(123))

# 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 
# 두 개의 문자열이 같으면 -1을 반환
def dif (s1, s2):

    length = min(len(s1), len(s2))

    for i in range(length):
        if s1[i] != s2[i]:
            return i
    return -1

# 출력
print(dif("hello", "hello"))
print(dif("hello", "helro"))

#문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
def index (s1, c1):
    li = []
    s1 = list(s1)
    for i in range(len(s1)):
        if s1[i] == c1:
            li.append(i)
            
    return li

print(index("hello", "l"))

#재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
def sumsum(num=100):
    if num== 1:
        return 1
    else:
        return num + sumsum(num-1)
    
print(sumsum())


