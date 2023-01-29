from pydantic import BaseModel
from typing import Optional, List

class User_DB(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    email: str
    # produtos: List[Product]
    # orders: List[Order]
    # sell: List[Order]

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    # user: User
    detail: str
    price: float
    available: bool = False

class Order(BaseModel):
    id: Optional[str] = None
    user: User_DB
    # product: Product
    quantity: int
    delivery: bool = False
    address: str
    observation: Optional[str] = 'No observations'