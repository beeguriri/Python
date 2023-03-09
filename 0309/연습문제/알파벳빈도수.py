# 주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.

text = "Hello, world!"

dic = {}

for char in text:
    if char.isalpha() :
        if char not in dic:
            dic[char] = 1
        else : 
            dic[char] += 1

print(dic)      
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}