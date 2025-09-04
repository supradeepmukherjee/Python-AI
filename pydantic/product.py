from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    inStock:bool=True

product1=Product(id=1,name='Laptop',price=999.99,inStock=True)
product2=Product(id=1,name='Laptop',price=999.99)
print(product1,product2)