from jose import jwt
from datetime import datetime, timedelta

# CONFIG
SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 60

def create_access_token(data_login: dict):
    data = data_login.copy()
    expires = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data.update({'exp': expires})

    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt

def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')
