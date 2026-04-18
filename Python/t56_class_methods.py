class  student():
    def __init__(self,aname,asection):
        self.name=aname
        self.section=asection
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leavos=newleaves
    def print(self):
        return f"Name is {self.name}. section is {self.section}"

harry=student("Harry",1) 
#larry=student()

'''
harry.name= "Harry"
harry.std=12
harry.section= 1
'''
harry.change_leaves(34)
print(harry.no_of_leavos)