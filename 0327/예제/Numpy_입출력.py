import numpy as np

# 단일 배열 저장
arr1 = np.array([1, 2, 3, 4, 5])
np.save('arr1.npy', arr1)  # 같은 디렉토리에 저장됨

# # 다중 배열 저장
# arr2 = np.array([1, 2, 3, 4, 5])
# arr3 = np.array([10, 20, 30, 40, 50])
# np.savez('arr.npz', arr2=arr2, arr3=arr3)
#
# # 배열 불러오기
loaded_arr1 = np.load('arr1.npy')
# loaded_data = np.load('arr.npz')
# loaded_arr2 = loaded_data['arr2']
# loaded_arr3 = loaded_data['arr3']

print(loaded_arr1)
