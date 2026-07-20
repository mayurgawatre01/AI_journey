import numpy as np
arr1d=np.array([1,2,3,4,45,6,6,78,89])
print(arr1d[-1])


import numpy as np
arr1d=np.array([1,2,3,4,45,6,6,78,89])
print(arr1d[1:])

import numpy as np
arr1d=np.array([1,2,3,4,45,6,6,78,89])
print(arr1d[::-1])



arr=np.array([10,20,30,40,50,60])
arr[1::2]=99
print(arr)

import numpy as np
arr1d=np.array([1,2,3,4,45,6,6,78,89])

arr1d[:7]=np.array([90,80,70,60,50,40,30])
print(arr1d)

print("original array",arr1d)


q=np.random.rand(3,3)

r=np.random.randn(3,3)
t=np.random.randint(10,size=(3,3))

print(q)
print(r)
print(t)