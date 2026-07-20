import numpy as np
arr=np.arange(-6,6).reshape(3,4)
print(arr)
print(np.abs(arr))
print(np.sqrt(arr))
print(np.square(arr))
print(np.exp(arr))
print(np.log2(arr))
print(np.sign(arr))


arr4d = np.random.randn(3, 4, 5, 2)
print(arr4d)