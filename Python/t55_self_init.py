class  student:
    def __init__(self,aname,asection):
        self.name=aname
        self.section=asection
    def print(self):
        return f"Name is {self.name}. section is {self.section}"

harry=student("Harry",1) 
#larry=student()

'''
harry.name= "Harry"
harry.std=12
harry.section= 1
'''
print(harry.print())