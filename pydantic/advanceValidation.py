from pydantic import BaseModel,field_validator,model_validator
from datetime import datetime

class Person(BaseModel):
    firstName:str
    lastName:str

    @field_validator('firstName','lastName')
    def namesMustBeCapitalized(cls,v):
        if not v.istitle():raise ValueError('Names must be capitalized')
        return v
    
class User(BaseModel):
    email:str

    @field_validator('email')
    def normalizeEmail(cls,v):
        return v.lower().strip()
    
class Product(BaseModel):
    price:str

    @field_validator('price',mode='before')
    def parsePrice(cls,v):
        if isinstance(v,str):
            return float(v.replace('$',''))
        return v
    
class DateRange:
    start:datetime
    end:datetime

    @model_validator(mode='after')
    def validateDateRange(cls,values):
        if(values.start>=values.end):raise ValueError('End must be after start')
        return values