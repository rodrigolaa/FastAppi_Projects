from sqlalchemy import Column, Integer, String
from infra.sqlalchemy.config.database import Base


class Serie_DB(Base):

    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genre = Column(String)
    year = Column(Integer)
    qnt_seasons = Column(Integer)
