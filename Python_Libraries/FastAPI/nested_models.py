from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
address_dic={'city': 'gurgaon','state':'haryana','pin':'122001'}
address1=Address(**address_dic)
Patient_dict={'name':'nitish','gender':'male','age':35,'address':address1}
patient1=Patient(**Patient_dict)
# print(patient1)
# print(patient1.name)
# print(patient1.address.city)
# print(patient1.address)

temp=patient1.model_dump(include=['name','gender'],exclude_unset=True)
print(temp)

temp2=patient1.model_dump_json(exclude={'address':['state']})
print(temp2)