from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.routing import APIRoute
from routers import product_router, user_router, orders_router

#create_bd()

app = FastAPI()

app.include_router(product_router.router)
app.include_router(user_router.router)
app.include_router(orders_router.router)



#CORS
orgins = [
'http//localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message":"Hello World"}