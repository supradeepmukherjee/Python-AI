from pydantic import BaseModel,Field
from typing import Optional
import re

class Employee(BaseModel):
    id:int
    name:str=Field(
        ...,
        min_length=3,
        max_length=50,
        description='Employee Name',
        examples='Supradeep Mukherjee'
    )
    dept:Optional[str]='General'
    salary:float=Field(
        ...,
        ge=10000
    )

class User(BaseModel):
    email:str=Field(
        ...,
        pattern=r''
    )
    phone:str=Field(
        ...,
        pattern=r'' 
    )
    age:int=Field(
        ...,
        ge=0,
        description="Age(in years)"
    )
    discounts:float=Field(
        ...,
        ge=0,
        lt=100,
        description='Discount Percentage'
    )