import numpy as np
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)


print(arr2d[1,2])
print(arr2d[-1,-2])

arr2d[0]=99
print(arr2d[:2])


print(arr2d[:,2])
print(arr2d[:,1:3])





arr_d = np.array([[10, 11, 12, 13],
                   [20, 21, 22, 23],
                   [30, 31, 32, 33]])
print(arr_d)

print(arr_d[:2,:2])


print(arr_d[::2,::3])