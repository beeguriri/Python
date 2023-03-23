import re


def extract_email(string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # /b~/b 사이의 문자열을 찾음
    # [대문자,소문자,숫자,.,_,%_,+,-]가 하나 이상 반복되는 문자열 => 아이디
    # @ 포함
    # [대문자,소문자,숫자,.,-]가 하나이상 반복되는 문자열 => 회사
    # \. 포함
    # [대문자 또는 소문자]{2글자 이상} => 도메인

    emails = re.findall(pattern, string)
    return emails


string = "John's email is john.doe123@example.com. Jane can be reached at jane@example.co.uk."

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # ^ : 문자열의 시작과 매칭
    # $ : 문자열의 끝과 매칭

    if re.match(pattern, email):
        return True
    else:
        return False


email1 = 'example@example.com'
email2 = 'example@example.co.kr'
email3 = 'example.example.com'
email4 = 'example@example.a'
email5 = 'example@example'

print(is_valid_email(email1))  # True
print(is_valid_email(email2))  # True
print(is_valid_email(email3))  # False
print(is_valid_email(email4))  # True
print(is_valid_email(email5))  # False
