from sqlalchemy.orm import Session
from  infra.sqlalchemy.models.models import Serie_DB
from schemas.schemas import Serie_Schema
from sqlalchemy import select, delete

class RepositorySerie():

    def __init__(self, db:Session):
        self.db = db

    def create(self, serie: Serie_Schema):
        db_serie = Serie_DB(
                            title = serie.title,
                            genre = serie.genre,
                            year = serie.year,
                            qnt_seasons = serie.qnt_seasons
                            )
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)

        return db_serie

    def list(self):
        series = self.db.query(Serie_DB).all()
        return series

    def obtain(self, serie_id: int):
        serie = self.db.query(Serie_DB).filter(Serie_DB.id == serie_id).first()
        return serie

    def remove(self, serie_id: int):

        # serie = self.db.query(Serie_DB).filter(Serie_DB.id == serie_id).first()

        # self.db.delete(serie)
        # self.db.commit()

        stmt = delete(Serie_DB).where(Serie_DB.id == serie_id)

        self.db.execute(stmt)
        self.db.commit()

        # self.db.refresh(serie)