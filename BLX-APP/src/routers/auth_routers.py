from routers.auth_utils import get_logged_in_user
from fastapi import status, Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repository.repository_users import RepositoryUser
from schemas.schemas import User_schema, User_schema_simple, User_schema_signin
from typing import List
from infra.sqlalchemy.providers import hash_provider, token_provider


router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=User_schema_simple)
def signup(user: User_schema, db: Session = Depends(get_db)):
    #verify if phone already exists:
    user_located = RepositoryUser(db).check_telephone_exists(user.phone)
    if user_located:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='phone number already registred in database')
    else:
        user.password = hash_provider.generate_hash(user.password)
        created_user = RepositoryUser(db).create(user)
        return created_user

@router.get("/users", status_code= status.HTTP_200_OK,response_model=List[User_schema_simple])
def list_users(db: Session = Depends(get_db)):
    users = RepositoryUser(db).list_all_users()
    return users

@router.get("/users/{id}", status_code= status.HTTP_200_OK,response_model=User_schema)
def list_users(id:int, db: Session = Depends(get_db)):
    user = RepositoryUser(db).show_user(id)
    return user

@router.delete("/users/{id}", status_code= status.HTTP_200_OK)
def list_users(id:int, db: Session = Depends(get_db)):
    user = RepositoryUser(db).show_user(id)
    return {"User {id} was deleted!"}


@router.post("/token", status_code=status.HTTP_201_CREATED)
def signin(user: User_schema_signin, db: Session = Depends(get_db)):
    #verify if phone already exists:
    phone = user.phone
    password = user.password

    user = RepositoryUser(db).check_telephone_exists(phone)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No User Registred with this Phone.')
    
    verified_password = hash_provider.verify_password(password, user.password)
    
    if not verified_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect password. Try again.')
    
    else:
        token = token_provider.create_access_token({'sub': user.phone})
        return {'username': user.name, 'id': user.id, 'access_token': token}
    

@router.get("/me", response_model=User_schema_simple)
def me( user: User_schema = Depends(get_logged_in_user)):
    return user
     

