f=open("p.txt","rt")

content=f.read()
print(content)

content=f.read()
print(content)


content=f.read()
print("1",content)

content=f.read()
print("2",content)


#line by char contant
'''
content=f.read()
for line in content:
print(line)
'''

#line by line
'''
#content=f.read()
for line in f:
    print(line,end="")
'''

'''
print(f.readline())
print(f.readline())
'''
print(f.readlines())

f.close()

