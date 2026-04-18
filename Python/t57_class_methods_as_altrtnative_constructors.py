class student:
    def __init__ (self,aname,asection):
        self.name=aname
        self.section=asection
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leavos=newleaves
    @classmethod
    def from_dash(cls,string):
        p=string.split("-")
        return cls(p[0],p[1])
    # def print(self):
    #     return f"Name is {self.name}. section is {self.section}"
harry=student("Harry",1) 
karan=student.from_dash("Karan-480")
#larry=student()
print(karan.section)
'''
harry.name= "Harry"
harry.std=12
harry.section= 1
'''