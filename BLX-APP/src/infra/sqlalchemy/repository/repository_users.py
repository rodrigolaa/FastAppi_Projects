from sqlalchemy import delete
from sqlalchemy.orm import Session
from schemas.schemas import User_schema
from infra.sqlalchemy.models.models import User_db

class RepositoryUser():
    
    def __init__(self, session:Session = None):
        self.db = session

    def create(self, user_scheme: User_schema):
        db_user = User_db(
            name = user_scheme.name,
            phone = user_scheme.phone,
            email = user_scheme.email,
            password = user_scheme.password,

            )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def list_all_users(self):
        users = self.db.query(User_db).all()
        return users

    def check_telephone_exists(self, phone: str):
        query = self.db.query(User_db).where(User_db.phone == phone).first()
        return query


    def show_user(self, user_id:int):
        user = self.db.query(User_db).where(User_db.id == user_id).first()
        return user

    #TODO DELETE ALL PRODUCTS OF THIS USER!
    def delete_user(self, user_id: int):
        delete_smt = delete(User_db).where(
            User_db.id == user_id
        )
        self.db.execute(delete_smt)
        self.db.commit()