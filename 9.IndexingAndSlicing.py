import numpy as np

# indexing
a=np.array([[1,2,3],[4,5,6]])
print(a)
print(a[0])   # this will print the first row of the 2D array

# slicing
print(a[1,2])   # this will print the value at second row and third column
print(a[:,1])   # this will print second column
print(a[1,:])   # this will print second row
print(a[1, :2]) # this will print all the columns upto second of second row
 
