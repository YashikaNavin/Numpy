import numpy as np
a=np.array([(1,2,3),(4,5,6)])

# Reshape data
print(a.reshape((3,2)))
b=np.reshape(a, (3,2), order='C')
print(b)

# Flatten data
print(b.flatten())  # this flatten() convert the multi-dimensional array or data into 1D array or data
