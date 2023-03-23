import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴을 다른 문자열로 대체하기
pattern = r"\d+"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

result1 = re.sub(pattern, "10", string1)
result2 = re.sub(pattern, "0", string2)
result3 = re.sub(pattern, "***", string3)

print(result1)  # I have 10 apples and 10 oranges
print(result2)  # The temperature is -0.0 degrees Celsius
print(result3)  # The password is ***
