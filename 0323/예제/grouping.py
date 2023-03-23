import re

# 전화번호에서 지역번호와 나머지 번호를 각각 추출
phone_number = "010-1234-5678"
pattern = r"(\d{2,3})-(\d{3,4})-(\d{4})"
result = re.match(pattern, phone_number)

area_code = result.group(1)
phone_number_without_area_code = result.group(2) + "-" + result.group(3)

print(area_code)  # 010
print(phone_number_without_area_code)  # 1234-5678

# YYYY-MM-DD => MM/DD/YYYY
date = "2022-03-18"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
result = re.sub(pattern, r"\2/\3/\1", date)

print(result)  # "03/18/2022"

# 이름 순서 바꾸기
string = "Kim, Yuna"
pattern = r"(\w+),\s*(\w+)" # \s 공백문자, * 앞의문자가 0번이상 반복
result = re.sub(pattern, r"\2 \1", string)
print(result)  # "Yuna Kim"
