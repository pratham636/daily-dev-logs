#list comprehensions
ls1=[i for i in range(100)]
ls=[i for i in range(100) if i%3==0]
print(ls1)
print(ls)
dict={0:"item0",1:"item1"}
#disctranli comprehensions
dict1={i:f"item{i}"for i in range(10) }
dict2={i:f"item{i}"for i in range(10) if i%3==0}
dict3={f"valu{i}":i for i in range(10) }
print(dict1)
print(dict)
print(dict2)
print(dict3)
#set comprehension
dresses={dress for dress in ["dress1","dress2","dress1","dress3","dress1"]}
print(dresses)
#genrater comprehension
evens=(i for i in range(100) if i%2==0 )
print(evens.__next__(),end=" ")
print(evens.__next__(),end=" ")
print(evens.__next__(),end=" ")
print(evens.__next__(),end=" ")
print(evens.__next__(),end=" ")