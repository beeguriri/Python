import numpy as np
"""
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(arr1[0])
print(arr1[-1])  # 제일 마지막 원소

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
print(arr2[0, 0])
print(arr2[1, 1])


# 브로드캐스팅
arr3 = np.array([1, 2, 3, 1])
arr4 = np.array([4, 5, 6, 7])

# 브로드캐스팅을 통해 크기가 다른 배열 간 연산이 가능
print(arr3 + arr4)  # [ 5  7  9 10]
"""


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# 배열 형태 변경
arr2d = arr.reshape((2, 4))
print(arr2d)

# 배열 구조 변경
arr2d_reshape = arr2d.reshape(4, 2)
print(arr2d_reshape)

# 배열 전치(Transpose)
arr2d_transpose = arr2d.T
print(arr2d_transpose)
