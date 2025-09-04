from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    postalCode:int

class User(BaseModel):
    id:int
    name:str
    email:str
    isActive:bool=True
    createdAt:datetime
    address:Address
    tags:List[str]=[]

    model_config=ConfigDict(
        json_encoders={datetime:lambda v:v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user=User(
    id=1,
    name='Supradeep',
    email='s@gmail.com',
    createdAt=datetime(2024,3,15,14,30),
    address=Address(
        street='fbgsufsfdui',
        city='fhghhwjsdved',
        postalCode=65477
    ),
    isActive=False,
    tags=['premium','subscriber']
)

print(user)
print('\n')

pyDict=user.model_dump()
print(pyDict)
print('\n')

jsonStr=user.model_dump_json()
print(jsonStr)