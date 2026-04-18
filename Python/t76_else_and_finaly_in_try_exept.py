f1=open("harry.txt")
try:
    f=open("does2.txt")
except EOFError as e:
    print("Print eof error aa gaya hai",e)
except IOError as e:
    print("Print IO error aa gaya hai",e)
else:
    print("Run this anyway...")
finally:
    print("Run this anyway...")
    f1.close()
print("Important stuff")