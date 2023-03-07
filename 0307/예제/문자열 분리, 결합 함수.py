# split( ) : 지정된 구분자(sep)로 나누어 리스트로 반환
string = "hello world"
string_list = string.split()  # 기본값인 공백을 구분자로 사용
print(string_list)  # ['hello', 'world']

string = "apple,banana,grape"
string_list = string.split(",")  # 쉼표를 구분자로 사용
print(string_list)  # ['apple', 'banana', 'grape']

#splitlines( ) :문자열을 개행 문자 또는 캐리지 리턴 문자 등을 기준으로 분리하여 
print("apple\nbanana\rgrape".splitlines())  # ["apple", "banana", "grape"]

#join( ) : 문자열을 반복 가능한 객체의 요소들을 구분자로 연결하여 반환합니다.
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"

