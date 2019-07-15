import numpy as np

# linspace() is used to give evenly spaced samples
a=np.linspace(1, 6, num=8)     # here endpoint is by default True which means the stop value is included
print(a)

b=np.linspace(1, 6, num=8, endpoint=False)   # here endpoint is False which means the stop value is excluded
print(b)

# logspace() is used to give even spaced numbers on log scale
c=np.logspace(1, 6, num=8)
print(c)

d=np.logspace(1, 6, num=8, endpoint=False)
print(d)
