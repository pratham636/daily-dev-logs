'''
def fun(num):     
    if num ==0:
        return print 
    if num==1:
        return sum
a=fun(0)
print(a)
'''

'''
def exe(fun):
    fun("This")
exe(print)
'''

def def1(fun1):
    def nowexe():
        print("Execute now")
        fun1()
        print("Executed")
    return nowexe

@def1
def who_is_harry():
    print("Harry is good boy.")
'''
who_is_harry=def1(who_is_harry)
who_is_harry()
'''
#or
who_is_harry()