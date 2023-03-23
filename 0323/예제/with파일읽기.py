with open("example.txt", "r", encoding="utf-8") as file:
    # 파일 내용 전체를 읽습니다.
    content = file.read()
    print("read() 함수 예시:")
    print(content)

    # 파일에서 한 줄을 읽습니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    line = file.readline()
    print("\nreadline() 함수 예시:")
    print(line)

    # 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    lines = file.readlines()
    print("\nreadlines() 함수 예시:")
    print(lines)
