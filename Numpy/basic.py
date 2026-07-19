import numpy as np
my_list=[1,2,3]
arr1d=np.array(my_list)
print(arr1d)


my_tensor=[[1,2,3],[1,2,4],[5,6,7]]
print(np.array(my_tensor))


my_tensor1 = [
    [[1, 2, 3],
     [4, 5, 6]],
    [[7, 8, 9],
     [10, 11, 12]],
    [[13, 14, 15],
     [16, 17, 18]]
]
arr3d = np.array(my_tensor1)
print(arr3d)


print(arr3d[:,1])

print(np.arange(0,21,2),np.arange(10,15))


print(np.linspace(1,10,19))

print(arr3d.dtype)



print(arr3d.astype(np.float64))

print(arr3d.astype(str))

print(arr3d.shape)

mayer_1=[[1,2,3],[4,5,6],[7,8,9]]
arr2d=np.array(mayer_1)
print(arr2d)


print(arr2d.shape)

print(arr2d.reshape(1,9))

print(arr2d.reshape(9,1))

print(arr3d.flatten())

print(arr3d.ravel())


print(arr3d.reshape(3,6))

#random number
one_random=np.random.rand(5,2)
print(one_random)

one_random1=np.random.randn(3,3)
print(one_random1)

one_random2=np.random.randint(0,10,5)
print(one_random2)


print(np.random.rand(2,3))
print(np.random.randn(3,3))
print(np.random.randint(1,10,size=(3,2)))

print(np.random.randn(3,3))