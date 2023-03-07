# 문자열 구성 파악 메소드 예시

# 문자열이 알파벳과 숫자로만 이루어졌는지 여부 확인
print("hello123".isalnum())  # True

# 문자열이 알파벳으로만 이루어졌는지 여부 확인
print("123".isalpha())  # False

# 문자열이 10진수 숫자로만 이루어졌는지 여부를 반환합니다.
print("123".isdecimal())  # True

# 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
print("123".isdigit())  # True

# 문자열이 파이썬 식별자로 사용 가능한지 여부를 반환합니다.
print("hello".isidentifier())  # True

# 문자열이 소문자로만 이루어졌는지 여부를 반환합니다.
print("hello".islower())  # True

# 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
print("123".isnumeric())  # True

# 문자열이 출력 가능한지 여부를 반환합니다.
print("Hello, World!".isprintable())  # True

# 문자열이 공백 문자로만 이루어졌는지 여부를 반환합니다.
print("   ".isspace())  # True
print("\t".isspace())  # True

# 문자열이 제목 케이스로 이루어졌는지 여부를 반환합니다.
print("Hello, World!".istitle())  # True

# 문자열이 대문자로만 이루어졌는지 여부를 반환합니다.
print("HELLO".isupper())  # True
