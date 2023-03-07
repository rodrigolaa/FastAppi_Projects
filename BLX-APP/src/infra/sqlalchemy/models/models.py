from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import  relationship #Object Relational Mapper ORM

class User_db(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    password = Column(String)

    products = relationship('Product_db', back_populates='users') #Refers to child class products relatonship one-to-may
    my_orders = relationship("Order_db", back_populates="users")

class Product_db(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)
    price = Column(Float)
    available = Column(Boolean)
    size = Column(String)

    user_id = Column(Integer, ForeignKey('user.id', name = "fk_product"))
    users = relationship('User_db', back_populates='products') 

class Order_db(Base):

    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    address = Column(String)
    type_delivery = Column(String)
    comments = Column(String)

    product_id = Column(Integer, ForeignKey('product.id', name = "fk_order_product"))
    user_id = Column(Integer, ForeignKey('user.id', name = "fk_order_users"))

    users= relationship('User_db', back_populates='my_orders') 
    product = relationship('Product_db') 
