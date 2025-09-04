from pydantic import BaseModel
from typing import Optional,List,Union

class Address(BaseModel):
    street:str
    city:str
    postalCode:int

class Company(BaseModel):
    name:str
    Address:Optional[Address]=None

class Employee(BaseModel):
    name:str
    company:Optional[Company]=None

class TxtContent(BaseModel):
    type:str='text'
    content:str

class ImgContent(BaseModel):
    type:str='img'
    url:str
    altText:str

class Article(BaseModel):
    title:str
    sections:List[Union[TxtContent,ImgContent]]

class Country(BaseModel):
    name:str
    code:str

class State(BaseModel):
    name:str
    country:Country

class City(BaseModel):
    name:str
    state:State

class Address(BaseModel):
    street:str
    city:City
    postalCode:str

class Organization(BaseModel):
    name:str
    headQuarter:Address
    branches:List[Address]=[]