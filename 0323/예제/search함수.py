import re

# 문자열 전체에서 정규표현식과 매칭되는 패턴 찾기
# 문자열 내에서 패턴을 검색하여 반환
pattern = r"[pP]ython"  # 첫글자 대소문자 구분없이 찾기
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())  # 매칭된 문자열: Python
else:
    print("매칭되지 않음")
