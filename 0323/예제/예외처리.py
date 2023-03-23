try:
    user_input = input("Enter a number: ")
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")

# 여러 예외 처리
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")

# 여러 예외를 별도의 except 블록으로 처리
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# as 키워드 사용
try:
    result = 5 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")

# 모든 예외 처리
try:
    # 예외가 발생할 수 있는 코드
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
except Exception as e:
    print(f"An error occurred: {e}")

# try-except-else 문
try:
    file = open("example.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
    file.close()

#try-except-finally 문
try:
    file = open("example.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied. You don't have the required permission to read this file.")
else:
    print("File content:")
    print(content)
finally: #무조건 실행
    if 'file' in locals() and not file.closed:
        file.close()
        print("File has been closed.")
