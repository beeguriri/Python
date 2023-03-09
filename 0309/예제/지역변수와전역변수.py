x = 1  # 전역 변수

def my_function():
    y = 2  # 지역 변수
    print('y:', y)  #y:2
    print('x:', x+1)  #x:2

my_function()
print('x:', x)  #x: 1

#함수 내부에서 global 키워드를 사용하면, 해당 변수는 전역 변수로 사용됨. 
x = 'hello'

def my_function():
    global x
    x = 'hi'

my_function()
print(x)    #hi

