# 부모 클래스
class People:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name : ", self.__name, "age : ", str(self.__age))

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name__(self, name):
        self.__name = name

# 상속받는 클래스
class Teacher(People):

    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)


t = Teacher(35, 'Kim', 'highschool')
t.introMe()
t.set_name__('Lee')
t.introMe()
t.showSchool()
