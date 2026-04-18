print("Enter a :")
a=input()
print("Enter b :")
b=input()

try:
    print("The sum of 2 number is", int(a)+int(b))
except Exception as e:
    print("Hello",e)
print("This line is very important")