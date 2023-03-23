# 파일 읽기
file = open("example.txt", "r", encoding="utf-8")

# 파일 내용 전체를 읽습니다.
content = file.read()
print("content : ", content)

# 파일에서 한 줄을 읽습니다.
line = file.readline()
print("line : ", line)  # lines : exampleaaa

# 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
lines = file.readlines()
print("lines : ", lines)  # lines : ['exampleaaa\n', 'ㄱㄱㄱ']

file.close()  # 파일을 닫습니다.
