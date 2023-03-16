class Calculator:

    # 생성자를 만들지 않아도 자동으로 호출

    # 클래스 변수
    operator = '+'

    # 클래스 메서드
    @classmethod
    def set_operator(cls, new_operator):
        cls.operator = new_operator

    # 인스턴스 메서드
    def calculate(self, num1, num2):
        if Calculator.operator == '+':
            return num1 + num2
        elif Calculator.operator == '-':
            return num1 - num2
        elif Calculator.operator == '*':
            return num1 * num2
        elif Calculator.operator == '/':
            return num1 / num2

# Calculator 클래스를 이용하여 객체 생성
my_calculator = Calculator()
print(my_calculator.calculate(2, 3)) # 출력 결과: 5

# 클래스 메서드 호출
Calculator.set_operator('*')
print(my_calculator.calculate(2, 3)) # 출력 결과: 6


