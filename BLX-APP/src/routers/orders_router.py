from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.schemas import Order_schema
from infra.sqlalchemy.repository.repository_order import RepositoryOrder
from infra.sqlalchemy.config.database import get_db
from typing import List 


router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED, response_model=Order_schema)
def create_order(order: Order_schema, session:Session = Depends(get_db)):
    order_created = RepositoryOrder(session).create_order(order)
    return order_created

@router.get("/orders/{user_id}", response_model = List[Order_schema] )
def list_order(user_id:int, session:Session = Depends(get_db)):
    orders= RepositoryOrder(session).list_orders_made_by_user(user_id=user_id)
    return orders

@router.get("/orders/{user_id}/sales", response_model = List[Order_schema] )
def list_sales(user_id:int, session:Session = Depends(get_db)):
    orders= RepositoryOrder(session).list_orders_sold_by_user(user_id=user_id)
    return orders

@router.get("/orders/{id}", response_model=Order_schema)
def show_order(id: int, session:Session = Depends(get_db)):
    order = RepositoryOrder(session).show_order_by_id(id)
    return order

@router.delete("/orders")
def delete_order(id: int, session:Session = Depends(get_db)):
    pass

@router.put("/orders")
def edit_order():
    pass