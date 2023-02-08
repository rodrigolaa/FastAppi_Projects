from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from schemas.schemas import Product_schema
from infra.sqlalchemy.models.models import Product_db

class RepositoryProduct():
    
    def __init__(self, session:Session = None):
        self.db = session

    def create_product(self, product: Product_schema):
        db_product = Product_db(
            name = product.name,
            detail = product.detail,
            price = product.price,
            available = product.available,
            user_id = product.user_id,
            size = product.size
            )

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def list_products(self):
        products = self.db.query(Product_db).all()
        # return jsonable_encoder(products)
        return products


    def edit_product(self, id:int, product_schema: Product_schema):
        update_stmt = update(Product_db).where(Product_db.id == id).values(
            name = product_schema.name,
            detail = product_schema.detail,
            price = product_schema.price,
            available = product_schema.available,
            size = product_schema.size
            )
        self.db.execute(update_stmt)
        self.db.commit()

    def delete_product(self, id: int):
        delete_smt = delete(Product_db).where(
            Product_db.id == id
        )
        self.db.execute(delete_smt)
        self.db.commit()