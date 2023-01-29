from fastapi import FastAPI, Depends
from schemas.schemas import Serie_Schema
from infra.sqlalchemy.repository.series import RepositorySerie
from infra.sqlalchemy.config.database import create_bd, get_db
from sqlalchemy.orm import Session

create_bd()

app = FastAPI()

@app.get("/")
def root():
    return {"Home"}


@app.post("/series")
def create_series(serie: Serie_Schema, db: Session = Depends(get_db)):
    serie = RepositorySerie(db).create(serie)
    return serie

@app.get("/series")
def create_series(db: Session = Depends(get_db)):
    series = RepositorySerie(db).list()
    return series

@app.get("/series/{serie_id}")
def obter_series(serie_id:int,db: Session = Depends(get_db)):
    serie = RepositorySerie(db).obtain(serie_id)
    return serie

@app.delete("/series/{serie_id}")
def obter_series(serie_id:int,db: Session = Depends(get_db)):
    RepositorySerie(db).remove(serie_id)
    return {"Message:":"Serie was removed successfully"}