# Numpy zeros and ones

import numpy as np

# zeros(shape,dtype,order) is a function which create an array of zeros of given shape
a=np.zeros((2,2), dtype=int, order='C')
print(a)
b=np.zeros((1,2,3))  # the other two arguments will be float64 and C respectively by default
print(b)

# ones(shape,dtype,order) is a function which create an array of 1,s of given size
c=np.ones((3,4), dtype=np.int32, order='C')
print(c)
d=np.ones((2,3,4))
print(d)
