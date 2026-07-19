import numpy as np
b=np.arange(1,13).reshape(3,4)
print(b)



total=b.sum()
total_m=b.mean()

axis_r=b.sum(axis=1)

print(axis_r)


axis_c=b.sum(axis=0)

print(axis_c)

print(b.max())
print(b.argmin())