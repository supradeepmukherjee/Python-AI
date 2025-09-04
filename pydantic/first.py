from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    isActive:bool

inputData={'id':'101','name':'dhfsfsh','isActive':478}

user=User(**inputData)
print(user)