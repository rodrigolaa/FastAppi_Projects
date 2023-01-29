from sqlalchemy.orm import Session
from scheme import schemes
from infra.sqlalchemy.models import models

class RepositoryUser():
    
    def __init__(self, db:Session = None):
        self.db = db

    def create(self, user_scheme: schemes.User_Schema):
        db_user = models.User_DB(
            name = user_scheme.name,
            phone = user_scheme.phone,
            email = user_scheme.email
            )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def to_list(self):
        users = self.db.query(models.User_DB).all()
        return users


    def obtain(self):
        pass

    def delete(self):
        pass