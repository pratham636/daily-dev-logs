f=open("p11.txt")
print(f.readline())

print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.tell())
