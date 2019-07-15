import numpy as np

# matmul() for matrix multiplication
a=np.array([[2,5],[6,9]])
b=np.array([[4.6,8.9],[2.7,3.8]])
print(np.matmul(a,b))

# linalg.det() is used to get the determinant of a matrix
print(np.linalg.det(a))
print(np.linalg.det(b))
