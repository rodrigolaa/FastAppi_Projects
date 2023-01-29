from sqlalchemy import Column, Integer, String, Boolean, Float
from infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import mapped_column

class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)
    price = Column(Float)
    available = Column(Boolean)

class User_DB(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)

#//TODO PROBLEM WITH  Type annotation for "User_DB.name" can't be correctly interpreted !
