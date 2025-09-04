from pydantic import BaseModel, computed_field,Field

class Product(BaseModel):
    price:float
    qty:int

    @computed_field
    @property
    def totalPrice(self)->float:return self.price*self.qty
    
class Booking(BaseModel):
    userID:int
    roomID:int
    nights:int=Field(...,ge=1)
    rate:float

    @computed_field
    @property
    def totalAmt(self)->float:return self.nights*self.rate

booking=Booking(
    userID=123,
    roomID=456,
    nights=3,
    rate=100
)

print(booking.totalAmt)
print(booking.model_dump())