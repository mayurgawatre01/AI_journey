import numpy as np
arr=np.array([10,20,30])

mask=arr>25
print(mask)


bol_arr=[True,False,False]*3
arr=np.arange(9)
print(arr[bol_arr])


arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

part=arr[:2]
filter=part[part>25]
print(filter)