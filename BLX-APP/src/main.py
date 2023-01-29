from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from sqlalchemy.orm import Session
from scheme.schemes import Product, User_Schema
from infra.sqlalchemy.repository.products import RepositoryProduct
from infra.sqlalchemy.repository.users import RepositoryUser
from infra.sqlalchemy.config.database import get_db, create_bd

create_bd()

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.post("/products")
def create_products(product: Product, db: Session = Depends(get_db)):
    created_product = RepositoryProduct(db).create(product)
    return created_product

@app.get("/products")
def list_products(db: Session = Depends(get_db)):

    products = RepositoryProduct(db).to_list()

    print(products)

    return products

@app.post("/users")
def create_users(user: User_Schema, db: Session = Depends(get_db)):
    created_user = RepositoryUser(db).create(user)
    return created_user

@app.get("/users")
def list_users(db: Session = Depends(get_db)):

    users = RepositoryUser(db).to_list()

    print(users)

    return users