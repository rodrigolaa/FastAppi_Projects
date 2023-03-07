from fastapi import FastAPI, Depends, Request, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.routing import APIRoute
from routers import product_router, auth_routers, orders_router
# from middlewares import timer

#create_bd()

app = FastAPI()

app.include_router(product_router.router)

#Security Routers authentication and authorization
app.include_router(auth_routers.router, prefix='/auth')

app.include_router(orders_router.router)

#Middlewares
@app.middleware('http')
async def time_procesor(request: Request, next):
        print('Interceptou a Chegada..')
        response = await next(request)
        print('Interceptou a Volta...')
        return response

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