# 변수이름앞에 "__" 붙이면 private변수로 바뀜
# 인스턴스에서 사용하려면 get, set함수 필요

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


p = Person("John", 30)
print(p.get_name())  # "John" 출력
p.set_name("Alice")
print(p.get_name())  # "Alice" 출력
