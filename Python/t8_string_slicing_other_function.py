from unicodedata import name

my_name="my sname is pratham"
print(len(my_name))
print(my_name[0:7])

#print(my_name[78]) #error
print(my_name[0:78])

#skip 1 chare
print(my_name[0:19:2])

print(my_name[3:])
print(my_name[:78])
print(my_name[::4])
print(my_name[::])

print(my_name[-3])
print(my_name[-4:])
print(my_name[-5:-2])

print(my_name[::-1])
print(my_name[::-2])

print(my_name.isalnum())
print(my_name.endswith("pratham"))
print(my_name.count("a"))
print(my_name.capitalize())
print(my_name.upper())
print(my_name.lower())
print(my_name.find("is"))
print(my_name.replace("is","are"))