from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from schemas.schemas import Order_schema, User_schema
from infra.sqlalchemy.models.models import Order_db

class RepositoryOrder():

    def __init__(self, db:Session) -> None:
        self.db = db

    def create_order(self, order: Order_schema):
        db_order = Order_db(
            product_id = order.product_id,
            user_id = order.user_id,
            quantity = order.quantity,
            address = order.address,
            type_delivery = order.type_delivery,
            comments = order.comments
            )

        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order
    
    def show_order_by_id(self, id:int):
        pass

    def list_orders_made_by_user(self, user_id:int):
        orders = self.db.query(Order_db).all()
        return orders

    def list_orders_sold_by_user(self, user_id:int):
        orders = self.db.query(Order_db).all()
        return orders

    def edit_order(self, id:int, order_schema: Order_schema):
        update_stmt = update(Order_db).where(Order_db.id == id).values(
            product_id = order_schema.product_id,
            quantity = order_schema.quantity,
            address = order_schema.address,
            type_delivery = order_schema.type_delivery,
            comments = order_schema.comments
            )
        self.db.execute(update_stmt)
        self.db.commit()

    def delete_order(self, id: int):
        delete_smt = delete(Order_db).where(
            Order_db.id == id
        )
        self.db.execute(delete_smt)
        self.db.commit()