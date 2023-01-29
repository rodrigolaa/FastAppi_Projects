from sqlalchemy.orm import Session
from scheme import schemes
from infra.sqlalchemy.models import models

class RepositoryProduct():
    
    def __init__(self, db:Session = None):
        self.db = db

    def create(self, product: schemes.Product):
        db_product = models.Product(
            name = product.name,
            detail = product.detail,
            price = product.price,
            available = product.available
            )

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def to_list(self):
        products = self.db.query(models.Product).all()
        # return jsonable_encoder(products)
        return products


    def obtain(self):
        pass

    def delete(self):
        pass