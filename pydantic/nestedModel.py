from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    postalCode:int

class User(BaseModel):
    id:int
    name:str
    address:Address

address=Address(
    street='f bdhnfbf',
    city='hbdsfbsfubhuaofgf',
    postalCode=12467
)

user=User(
    id=1,
    name='hjehfbjef',
    address=address
)

userData={
    'id':1,
    'name':'fsfsfbj',
    'address':{
        'street':'gyadigdy',
        'city':'davhsb',
        'postalCode':67834
    }
}

user=User(**userData)
print(user)