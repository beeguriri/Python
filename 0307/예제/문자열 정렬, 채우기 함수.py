# 문자열 정렬, 채우기 함수
s = "hello"

#center(width[, fillchar]): 문자열을 지정된 너비(width) 가운데 정렬하여 새로운 문자열을 반환합니다. 
#fillchar 인자를 지정하면 문자열을 채우는데 사용할 문자를 지정할 수 있습니다. 기본값은 공백입니다.
print(s.center(10))  # "  hello   "
print(s.center(11, "-"))  # "---hello---"

#ljust(width[, fillchar]): 문자열을 지정된 너비(width)에 맞추어 왼쪽으로 정렬하여 새로운 문자열을 반환합니다. 
#fillchar 인자를 지정하면 문자열을 채우는데 사용할 문자를 지정할 수 있습니다. 기본값은 공백입니다.
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"

#rjust(width[, fillchar]): 문자열을 지정된 너비(width)에 맞추어 오른쪽으로 정렬하여 새로운 문자열을 반환합니다. 
#fillchar 인자를 지정하면 문자열을 채우는데 사용할 문자를 지정할 수 있습니다. 기본값은 공백입니다.
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"

#zfill(width): 문자열의 왼쪽에 0을 채워서 지정된 너비(width)에 맞추어 새로운 문자열을 반환합니다.
print("123".zfill(5))  # "00123"