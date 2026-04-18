from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List ,Dict,Optional,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of patient less than 50 character',examples='Nitish')]
    email:EmailStr
    age:int=Field(gt=0 ,lt=120)
    # weight:float = Field(gt=0)
    weight:Annotated[float,Field(gt=0,strict=True)]
    # married:bool =False
    height:float
    married:Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies:Optional[List[str]]=Field(default=None,max_length=5)
    contact_details:Dict[str,str]
    url:AnyUrl

    @computed_field
    @property
    def bmi_1(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    @field_validator('email')
    @classmethod
    def email_validater(cls,value):
        valid_domains=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name',mode='before')
    @classmethod
    def trasform_name(cls,value):
        return value.upper()
    
    @model_validator(mode='after')
    def validate_emergancy_number(self):
        if self.age>60 and 'emergency' not in self.contact_details:
            raise ValueError('Pations older than 60 must have contact')
        return self



def inset(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)
    print('bmi',patient.bmi_1)
    print("inserted")

Patient_info={'name':'nitish','email':'abc@hdfc.com','age':65,'weight':75.3,'height':1.72,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','number':'42332432','emergency':'530947'},'url':'httm://linkin.com'}

patient1=Patient(**Patient_info)
inset(patient1)