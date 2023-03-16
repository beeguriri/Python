class Student:
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score

    # 학생정보 문자열로 반환
    def get_info(self):
        return f"이름 : {self.name}, 학번 : {self.student_id}, 학년 : {self.year}, 전공 : {self.major}, 평점 : {self.avg_score}"


class StudentManager:
    def __init__(self):
        self.student_list = []

    # 학생을 리스트에 추가
    def add_student(self, student):
        self.student_list.append(student)

    # 학번을 이용해 학생을 리스트에서 제거하는 메서드
    def remove_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                print(f"{student_id} 삭제")
                return
        print(f"{student_id}학번을 가진 학생이 없습니다.")

    # 학번을 이용해 학생을 찾는 메서드
    def find_student(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                print(student.get_info())
                return
        print(f"{student_id}학번을 가진 학생이 없습니다.")

# 모든 학생의 정보를 출력하는 메서드
    def show_all_students(self):
        for student in self.student_list:
            print(student.get_info())


sm = StudentManager()

student1 = Student("홍길동", '20230001', '2', '컴퓨터공학', 90.5)
student2 = Student("가나다", '20210007', '1', '전자공학', 89.0)
student3 = Student("ABC", '20200001', '4', '건축공학', 91.2)
print("========== insert ==========")
sm.add_student(student1)
sm.add_student(student2)
sm.add_student(student3)
sm.show_all_students()
print("========== find ==========")
sm.find_student('20230001')
sm.find_student('20230011')
print("========== remove ==========")
sm.remove_student('20230001')
sm.remove_student('20230123')
