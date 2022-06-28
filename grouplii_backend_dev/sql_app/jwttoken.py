from functools import lru_cache
from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import schemas
from . import config


@lru_cache()
def get_settings():
    return config.Settings()

SECRET_KEY = get_settings().SECRET_KEY
ALGORITHM = get_settings().ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = get_settings().ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credentials_exception):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception
		token_data = schemas.TokenData(username=username)
	except JWTError:
	    raise credentials_exception