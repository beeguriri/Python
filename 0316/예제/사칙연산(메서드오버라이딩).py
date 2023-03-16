class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

class AdvancedCalculator(Calculator):
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b

c = Calculator()
print(c.add(2, 3))        # 5
print(c.subtract(5, 1))   # 4
print(c.multiply(4, 6))   # 24
print(c.divide(10, 2))    # 5.0

ac = AdvancedCalculator()
print(ac.divide(10, 0))   # Cannot divide by zero
print(ac.divide(10, 2))   # 5.0
