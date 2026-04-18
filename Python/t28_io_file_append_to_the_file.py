#f=open("p11.txt","w")
'''
f=open("p11.txt","a")
a=f.write("Pratham is the good boy.\n")     
print(a)
f.close()
'''
# handle read and write both

f=open("p11.txt","r+")
print(f.read())
f.write("thank you")
