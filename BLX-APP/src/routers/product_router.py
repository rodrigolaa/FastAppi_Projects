from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.schemas import Product_schema, Product_simple
from infra.sqlalchemy.repository.repository_products import RepositoryProduct
from infra.sqlalchemy.config.database import get_db
from typing import List 


router = APIRouter( )

@router.post("/products", status_code=status.HTTP_201_CREATED, response_model=Product_simple)
def create_products(product: Product_schema, session: Session = Depends(get_db)):
    created_product = RepositoryProduct(session).create_product(product)
    return created_product

@router.get("/products", status_code= status.HTTP_200_OK,response_model=List[Product_schema])
def list_products(session: Session = Depends(get_db)):
    products = RepositoryProduct(session).list_products()
    return products

@router.put("/products/{id}")
def edit_product(id:int, product: Product_schema, session: Session = Depends(get_db)):
    RepositoryProduct(session).edit_product(id,product)
    return {"message:": f"Product {product.name} was updated!" }

@router.delete("/products/{id}", status_code= status.HTTP_200_OK)
def delete_product(id: int, session: Session = Depends(get_db)):
    RepositoryProduct(session).delete_product(id)
    return {"message:": f"Product id: {id} was deleted!" }