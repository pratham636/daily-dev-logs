import numpy as np
a=np.array([1,2,3],dtype='int16')
print(a)
b=np.array([[9,8,7],[6,5,4]])
print(b)

# Get Dimension
print(a.ndim)
print(b.ndim)

# Get Shape
print(a.shape)
print(b.shape)

# get type
print(a.dtype)
print(type(a))
print(b.dtype)

#get size
print(a.itemsize)
print(b.itemsize)

#Get total size
print(a.nbytes)
print(b.nbytes)
