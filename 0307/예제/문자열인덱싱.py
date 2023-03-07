#문자열에서 짝수/홀수번째 문자 추출하기

string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]

print(result)  # 출력값: "acegi"



string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 != 0:
        result += string[i]

print(result)  # 출력값: "bdfhj"
