# 부모 클래스
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("안녕하세요, 제 이름은", self.name, "입니다.")
        print("나이는", self.age, "살입니다.")


# 상속받는 클래스
class Teacher(People):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().introduce()
        print("제 전공은", self.subject, "입니다.")


teacher = Teacher("홍길동", 30, "수학")
teacher.show_info()
