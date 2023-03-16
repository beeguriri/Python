"""
다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라.
Employee 클래스에 employeeID 인스턴스 변수를 추가하고 getID() 메소드를 정의하라.
getID() 메소드는 employeeID를 반환하는 메소드이다.
Employee 클래스를 이용하여
Employee("동양", 65, 2019)로 생성된 객체의 이름, 나이, ID를 출력하라.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID = employeeID

    def getID(self):
        return self.employeeID


e = Employee('동양', 65, '2019')
print(f'이름 : {e.getName()}, 나이 : {e.getAge()}, ID : {e.getID()}')
