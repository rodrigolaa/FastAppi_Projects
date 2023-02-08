from fastapi import status, Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repository.repository_users import RepositoryUser
from schemas.schemas import User_schema
from typing import List


router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: User_schema, db: Session = Depends(get_db)):
    created_user = RepositoryUser(db).create(user)
    return created_user

@router.get("/users", status_code= status.HTTP_200_OK,response_model=List[User_schema])
def list_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).to_list()
    return users