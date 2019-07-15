import numpy as np

# Creating numpy array
# 1st way:- create a list and then provide that list as argument in array()
mylist=[1,2,3,4,5]
a=np.array(mylist)
print(a)
# 2nd way:- directly pass the list as an argument within the array()
b=np.array([6.5,7.2,8.6,9,10])
print(b)

# Creating one more numpy array
c=np.array(['Hi', 1, 'Hello', 2])
print(c)

# Mathematical operations on array
print(a+10)
print(b-56)
#print(c*2) # can't perform mathematical operations with string data type
print(a*2)

# To know the shape(size) and data type of array
print(a.shape)
print(a.dtype)
print(b.shape)
print(b.dtype)

# Creating 2D array
d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(d)
print(d.shape)

# Creating 3D array
e=np.array([[[1,2],[3,4]],
            [[5,6],[7,8]],
            [[9,10],[11,12]]])
print(e)
print(e.shape)