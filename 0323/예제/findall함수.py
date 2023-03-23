import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴 찾기
pattern = r"\d+"  # 1글자 이상의 숫자 찾기
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

matches1 = re.findall(pattern, string1)
matches2 = re.findall(pattern, string2)
matches3 = re.findall(pattern, string3)

print(matches1)  # ['2', '3']
print(matches2)  # ['-1', '5']
print(matches3)  # ['12345678']

# 010[- ]\d{4}[- ]\d{4} => 010-1234-1572 / 010 1232 4444
# 010[- ]+\d{4}[- ]+\d{4} => 010 - 1234 - 1234
