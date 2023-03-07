# 문자열 슬라이싱
"""
string[start:end:step]
인자 생략 시 start는 0, end는 문자열의 길이, step은 1
"""

string = "hello world"

# end, step 생략
substring = string[6:]
print(substring)  # "world"

# start, step 생략
substring = string[:5]
print(substring)  # "hello"

# step 생략
substring = string[1:5]
print(substring)  # "ello"

# start, end 생략
substring = string[::2]
print(substring)  # "hlowrd"

# 문자열 뒤집기
reversed_s = string[::-1]
print(reversed_s)  # "dlrow olleh"

# 문자열 뒤집기2
reversed_s = string[::-2]
print(reversed_s)  # "drwolh"