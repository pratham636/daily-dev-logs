class a:
    def __init__(self):
        self.va1="a"
        self.vars="a"
class b(a):
    def __init__(self):
        super().__init__()
        self.vars="b"
s=a()
p=b()
print(p.vars)
print(p.va1)