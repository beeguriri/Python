class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

# 메서드 오버라이딩을 이용한 다형성 구현
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak() # 각 객체에 따라 다른 동작을 수행
