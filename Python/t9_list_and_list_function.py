from distutils.util import change_root
import numbers
from re import X


grocery=["Haepic","Vim bar","Deodrant","Bhindi","Lollypop",20]
print(grocery)
print(grocery[5])

number=[1322,312231,4243,5,34342,676]
print(number)
print(number[3])
number.sort()
print(number)
number.reverse()
print(number)
print(number[0:2])

number.append(7)
print(number)

number.insert(2,56)
print(number)
number.remove(56)
number.pop()
number.pop()
print(number)

#mutable - can change
#immutable - can not change

#typeles in python
a=()
a1=(1)
b=(1,)
c=(1,2,3,4,5)
d=('harry',5,'demo',5.8)
print(a,a1,b,c,d)

x=3
y= 5
x,y=y,x
print(x,y)