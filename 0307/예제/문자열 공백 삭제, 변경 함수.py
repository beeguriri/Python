# 문자열 공백 삭제 및 변경 함수 예시
s = "  hello,   world!  "

#strip([chars]): 문자열의 양쪽 끝에서 지정된 문자(chars)를 제거한 새로운 문자열을 반환합니다. 
#chars 인자를 생략하면 공백을 제거합니다.
print(s.strip())  # "hello,   world!"

#lstrip([chars]): 문자열의 왼쪽 끝에서 지정된 문자(chars)를 제거한 새로운 문자열을 반환합니다. 
# chars 인자를 생략하면 공백을 제거합니다.
print(s.lstrip())  # "hello,   world!  "

#rstrip([chars]): 문자열의 오른쪽 끝에서 지정된 문자(chars)를 제거한 새로운 문자열을 반환합니다. 
# chars 인자를 생략하면 공백을 제거합니다.
print(s.rstrip())  # "  hello,   world!"

#replace(old, new[, count]): 문자열에서 old를 new로 바꾼 새로운 문자열을 반환합니다. 
# count 인자를 사용하면 치환할 최대 횟수를 지정할 수 있습니다.
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   world!  "
