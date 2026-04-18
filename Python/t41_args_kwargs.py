def fun (normal,*arg,**kwarg):  #sycvans first nornal,args,kwargs
    print(normal)
    for key in arg:
        print(f"{key} is")
    for key,value in kwarg.items():
        print(f"{key} is a {value}")      

har=["Harry","Rohan","skillf"]
normal="This is normal function"
kw={"harry":"Monitor","Harry":"Fitmess Instructer"}
fun(normal,*har,**kw)    