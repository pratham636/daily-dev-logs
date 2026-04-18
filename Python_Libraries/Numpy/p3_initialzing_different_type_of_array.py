import numpy as np
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#All 0s matrix
print(np.zeros((2,3,4)))

#All 1s matrix
print(np.ones((2,3,4)))

# Any other number
print(np.full((2,3),99, dtype='float32'))
print(np.full((2,3),99))

#Any other number (full_like)
print(np.full_like(a,4))
print(np.full(a.shape,4))

#Random decimal numbers
print(np.random.rand(4,2))
print(np.random.randint(0,9,9)) #Start index,End index,Total number
print(np.random.randint(7,size=(3,3)))
print(np.random.randint(4,7,size=(3,3))) #Start index,End index,Total number

#identity matrix
print(np.identity(9))

#repet an array 
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)


#careful to copyint array
a1=np.array([1,2,3])
c1=a1.copy()
c1[0]=100
print("c1 ",c1,"a1 ",a1)
b1=a1
b1[0]=100
print("b1 ",b1,"a1 ",a1)
