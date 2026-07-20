import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
y=np.array([20,30,40,50,60,70,80,90])

condition=np.array([True,False,True,False,True,False,True,False])

result=np.where(condition,x,y)
print(result)

salary = np.array([25000, 40000, 18000, 50000])

result1=np.where(salary>=25000,"high","low")
print(result1)

arr=np.random.randn(3,3)
print(arr)

x=np.where(arr>0,1,-1)
print(x)







arr3d = np.random.randn(4, 3, 2)
print(arr3d)

