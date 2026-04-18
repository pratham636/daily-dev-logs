d1={}
d2={"Harry":"burger","Rohan":"Fish","Skillf":"Roti","Shubham":{"B":"Maggi","L":"Roti","D":"chicken"}}
print(d1)
'''print(d2)
print(d2["Harry"])
print(d2["Shubham"])
print(d2["Shubham"]["L"])
'''
d2["Ankit"]="Junk Food"

d2[420]="Kababs"
print(d2)
del d2[420]
print(d2)
#d3=d2   #d2 and d3 point in same dictionary
d3=d2.copy()
del d3["Harry"]
print(d3)
print(d2)



print(d2.get("Harry"))
d2.update({"Leena":"Toffee"})
print(d2)
print(d2.keys())
print(d2.items())