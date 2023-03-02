# % 연산자를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is %s, I'm %d years old, and my height is %.3f" % (name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."

# 문자열
name = "John"
print("Hello, %s!" % name)

# 정수
num = 42
print("The answer is %d." % num)

# 실수
pi = 3.14159
print("Pi is approximately %.G." % pi)

# 여러 개의 변수
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is %s %s and I am %d years old." % (first_name, last_name, age))





# format() 메소드를 이용한 포매팅
name = "John"
age = 30
height = 175.5

print("My name is {0}, I'm {2} years old, and my height is {1}.".format(name, age, height))
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."





# f-string을 이용한 문자열 포매팅
name = "John"
age = 30
height = 175.5

print(f"My name is {name}, I'm {age} years old, and my height is {height:.1f}.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.5."