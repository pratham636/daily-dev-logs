from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str="John Doe"
    signup_ts:datetime|None=None
    friends:list[int]=[]

external_data={
    "id":"123",
    "signup_ts":"2017-06-01 12:22",
    "friends":{1,"2","3"},
}
User=User(**external_data)
print(User)
print(User.id)