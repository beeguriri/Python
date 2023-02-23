# 포매팅실습
"""
My name is {Tom} and I am {20} years old.
I have {3} apples, {2} oranges, and {1} banana.
The result is {1.23}.
Your score is {90}%.
{10} + {20} = {30}
"""

name = "Tom"
age = 20
print(f"My name is {name} and I am {age} years old.")

fruit = [3,2,1]
print(f"I have {fruit[0]} apples, {fruit[1]} oranges, and {fruit[2]} banana.")

result = 1.23
print(f"The result is {result:10.3f}.") #결과:      1.230
print(f"The result is {result:0>10.2f}.") #결과 : 0000001.23

score = 90
print(f"Your score is {score}%.")

a=10
b=20
print(f"{a} + {b} = {a+b}")

