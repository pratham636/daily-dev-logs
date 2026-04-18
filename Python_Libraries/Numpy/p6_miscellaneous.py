import numpy as np


#Load Data From File
a=np.genfromtxt('data.txt',delimiter=',')
print(a.astype('int32')) # copy of a
print(a)
a=a.astype('int32') # a change
print(a)


#Boolean makeing and Advanced indexing
print(a > 50)
print(a[a>50]) #index greater then 50

#INdex with list b in numpy
b=np.array([1,2,3,4,5,6,7,8,9])
print(b[[1,2,3,8]])
print(np.any(a>50, axis=0))
print((a>50) & (a<100))
print(~((a>50) & (a<100))) # ~ use for not
 