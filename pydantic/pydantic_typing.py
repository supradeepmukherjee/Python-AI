from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    userID:int
    items:List[str] # str is from pydantic
    qty:Dict[str,int]

class BlogPost(BaseModel):
    title:str
    content:str
    imgUrl:Optional[str]=None

cartData={
    'userID':123,
    'items':['Laptop','Mouse','Keyboard'],
    'qty':{'Laptop':1,'Mouse':2,'Keyboard':3}
}

cart=Cart(**cartData)