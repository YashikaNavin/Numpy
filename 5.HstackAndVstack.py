import numpy as np

# hstack() used to append the arrays horizontally
a=np.array([1,2,3])
b=np.array([4,5,6])
print("Horizontal Append: ", np.hstack((a,b)))

# vstack() used to append the arrays vertically
print("Vertical Append: ", np.vstack((a,b)))


# random.normal(loc, scale, size) to generate random numbers where loc=mean, scale=standard deviation and size=number of random numbers
c=np.random.normal(6, 0.9, 6)
print(c)
