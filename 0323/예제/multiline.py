import re

string = """Python is an interpreted language
Python is an interpreted language
It is dynamically typed
And it is easy to learn"""

pattern = '^Python'
result = re.findall(pattern, string, re.M)
print(result)  # ['Python', 'Python']
