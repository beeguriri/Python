#입력한 문자열에서 모음(a, e, i, o, u)을 제거하는 프로그램

vowels = ['a', 'e', 'i', 'o', 'u']
input_str = input("Enter a string: ")

output_str = ""
for char in input_str:
    if char in vowels:
        pass
    else:
        output_str += char

print("Modified string:", output_str)
