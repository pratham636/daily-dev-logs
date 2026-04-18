s = set()

print(type(s))
s_from_list=set([1,2,3,4])
l=[1,2,3,4,5]
s_from_list=set(l)
print(s_from_list)
print(type(s_from_list))

s.add(1)
#s.add(1)# print unique
s.add(2)
s1=s.union({2,3})
s2={4,5}
print(s1)
print(s1.isdisjoint(s2)) # unequle                           
print(s)
s.remove(2)
print(s)