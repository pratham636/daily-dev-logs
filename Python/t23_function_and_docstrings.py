#build in function
a=8
b=9
x=sum((a,b))
print(x)

def fun1(a,b):
    print("Hello you are in function 1 = ",a+b)

def fun2(a,b):
    #tbhis is dotstring
    """This number does not work for 3 numbers."""
    print("Hello you are in function 2 = ",a*b)

print(fun1(3,4))
print(fun2(3,4))
print(fun2.__doc__)