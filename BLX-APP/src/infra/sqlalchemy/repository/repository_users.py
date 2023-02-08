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
            senha = user_scheme.senha,

            )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def to_list(self):
        users = self.db.query(User_db).all()
        return users


    def obtain(self):
        pass

    def delete(self):
        pass