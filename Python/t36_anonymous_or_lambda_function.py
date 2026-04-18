import numbers


numbers=lambda n1,n2,n3:n1+n2+n3
print(numbers(10,28,34))

a=[[178,1489],[5,6],[38,23]]
a.sort(key=lambda x:x[1])
print(a)
