"""
for 루프를 이용하여 다음과 같은 리스트를 생성하라.
0~49까지의 수로 구성되는 리스트
1~50까지 수의 제곱으로 구성되는 리스트
"""
list1 = [num for num in range(0,50)]
print(list1)

list2 = [num**2 for num in range(1,51)]
print(list2)

a_list = []
for i in range(0,50) :
    a_list.append(i)
print(a_list)

"""
크기가 같은 두 개의 리스트 L, M을 생성하고 두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하라. 
예를 들어 L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]인 리스트 생성
"""
l = [1,2,3]
m = [4,5,6]
n = []
for i in range(0, len(l)):
    n.append(l[i]+m[i])
print(n)

n1 = [l[i]+m[i] for i in range(0, len(l))]
print(n1)

"""
사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열을 생성하라. 
예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.
"""
num = [2,5,11,33,55]
string = ['+'+str(nums) for nums in num if nums != num[0]]
result = str(num[0])
for st in string:
    result += st
print(result)


num1 = "2 5 11 33 55"
num1_list = num1.split()
result = "+".join(num1_list)
print(result)