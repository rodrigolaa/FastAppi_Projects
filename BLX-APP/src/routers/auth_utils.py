from infra.sqlalchemy.repository.repository_users import RepositoryUser
from infra.sqlalchemy.config.database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from requests import Session
from infra.sqlalchemy.providers import token_provider
from jose import JWTError


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_logged_in_user(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):
    # Decode token, get phone, search user with this phone, and retrieve user info.
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalid')
    try:
        phone = token_provider.verify_access_token(token)
    except JWTError:
        raise exception
    
    if not phone:
        raise exception
    
    user = RepositoryUser(session=session).check_telephone_exists(phone)

    if not user:
        raise exception

    return user
    