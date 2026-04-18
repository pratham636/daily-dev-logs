import numpy as np
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

#get specific element [r, c]
print(a[1,6])
print(a[0,-1])

#get specific row
print(a[0,:])

#get specific column
print(a[:,3])

#    [Startindex, Endindex, Stepsize]
print(a[0,1:6:2])

a[1,5]=20
print(a)

a[:,2]=5
print(a)

# 3D array

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Specific element element (work outside in)
print(b[0,1,1])
print(b[:,0,:])
b[:,0,:]=[[2,2],[2,2]]
print(b)