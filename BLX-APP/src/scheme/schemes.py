from pydantic import BaseModel
from typing import Optional, List

class User_Schema(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
    email: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    detail: str
    price: float
    available: bool = False

    class Config:
        orm_mode = True

class Order(BaseModel):
    id: Optional[str] = None
    user: User_Schema
    # product: Product
    quantity: int
    delivery: bool = False
    address: str
    observation: Optional[str] = 'No observations'