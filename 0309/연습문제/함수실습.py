#1~n까지의 합을 계산하는 함수

def numsum(num) :
    temp = [num for num in range(1,num+1)]
    return sum(temp)

print(numsum(10))

# 반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와 
# 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라. 
# 이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래 첫 자리까지 구하라.

def cir_area(r) :
    return 3.14*r*r

def cir_cirm(r) :
    return 2*3.14*r

print("area : %.1f" %cir_area(3.5))
print("area :",round(cir_area(3.5),1))

print("cirm : %.1f" %cir_cirm(3.5))

# den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성
#12 -> [1, 2, 3, 4, 6, 12]

def den(n) :
    cd = []
    for i in range(1,n+1):
        if n%i==0:
            cd.append(i)
    return cd

def den2(n) :
    result = [i for i in range(1,n+1) if n%i==0]
    return result

print(den(12))
print(den2(12))