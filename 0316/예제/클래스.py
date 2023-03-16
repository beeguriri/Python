class Rectangle:
    # 클래스변수
    count = 0

    # 생성자
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1  # 클래스 호출될때마다 증가

    # 인스턴스 메서드
    def area(self):
        return self.width * self.height

    # 클래스 메서드
    @classmethod
    def print_count(cls):
        print(cls.count)


print("count", Rectangle.count)  # 출력 결과: 0
Rectangle.print_count()  # 클래스 메서드 사용

# 인스턴스 생성
rectangle1 = Rectangle(3, 4)
print("count", Rectangle.count)  # 출력 결과: 1
Rectangle.print_count()

rectangle2 = Rectangle(5, 6)
print("count", Rectangle.count)  # 출력 결과: 2
Rectangle.print_count()

# 인스턴스 변수에 접근하여 값 출력
print(rectangle1.width)  # 출력 결과: 3
print("count", Rectangle.count)  # 출력 결과: 3

print(rectangle1.height)  # 출력 결과: 4
print(rectangle2.width)  # 출력 결과: 5
print(rectangle2.height)  # 출력 결과: 6

# 인스턴스 메서드 호출
print(rectangle1.area())  # 출력 결과: 12
print(rectangle2.area())  # 출력 결과: 30

# 인스턴스 변수 값 변경
rectangle1.width = 5
print(rectangle1.width)  # 출력 결과: 5

# 인스턴스 메서드 호출
print(rectangle1.area())  # 출력 결과: 20
