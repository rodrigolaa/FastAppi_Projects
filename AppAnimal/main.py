from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers = ['*']
)
class Animal(BaseModel):
    id: int
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get("/animais")
def listar_animais():
    return banco

@app.get("/animais/{id}")
def obter_animal(id: str):
    for animal in banco:
        if animal.id == id:
            return animal
    return {"error":"Animal not found"}

@app.delete("/animais/{id}")
def deletar_animal(id: str):
    posicao = -1
    for index,animal in enumerate(banco):
        if animal.id == id:
            posicao = index
            banco.pop(posicao)
            return {"mensagem:" : "Animal removido com sucesso!"}
            break
    return {"error":"Animal not found"}

@app.post("/animais")
def criar_animais(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)

