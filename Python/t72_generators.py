def gen(n):
    for i in range(n):
        yield i
q=gen(5)
print(q.__next__())
print(q.__next__())
print(q.__next__())
