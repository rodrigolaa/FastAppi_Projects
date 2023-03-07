from pydantic import BaseModel
from typing import Optional, List


class Product_simple(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    available: bool

    class Config:
        orm_mode = True

class User_schema_simple(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str

    class Config:
        orm_mode = True

class User_schema(BaseModel):
    id: Optional[int] = None
    name: str
    phone: str
    email: str
    password: str
    products: List[Product_simple] = []

    class Config:
        orm_mode = True

class User_schema_signin(BaseModel):
    password: str
    phone: str
    
    class Config:
        orm_mode = True

class Product_schema(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int]
    name: str
    detail: str
    price: float
    available: bool = False
    size: Optional[str] = None
    users: Optional[User_schema_simple]

    class Config:
        orm_mode = True

class Order_schema(BaseModel):
    id: Optional[str] = None
    quantity: int
    address: Optional[str]
    type_delivery: str
    comments: Optional[str] = 'No observations'

    user_id: Optional[int]
    product_id: Optional[int]

    user: Optional[User_schema_simple]
    product: Optional[Product_simple]

    class Config:
        orm_mode = True