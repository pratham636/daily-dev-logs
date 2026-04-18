import numpy as np
a=np.array([1,2,3,4])
print(a)

print(a+2)
print(a-2)
print(a/2)

b=np.array([1,0,1,0])
print(a+b)
print(a**2)

#Take the sin,cos
print(np.sin(a))
print(np.cos(a))


# Linear Algebra
a=np.ones((2,3))
print(a)
b=np.full((3,2),2)
print(b)
print(np.matmul(a,b))

c=np.identity(3)
print(np.linalg.det(c))

#statistics
stats=np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.min(stats,axis=1))
print(np.max(stats))
print(np.sum(stats))