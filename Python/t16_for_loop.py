'''list1=["Harry","Larry","Carry","Marie"]

for item in list1:
    print(item)
'''
list1=[ ["Harry",1] , ["Larry",2] , ["Carry",6] , ["Marie",250] ]

for item,lollypop in list1:
    print(item, "and lollypop is ",lollypop)

dict1=dict(list1)
print(dict1)

for item,lollypop in dict1.items():
    print(item, "and lollypop is ",lollypop)

