import bcrypt
from jose import jwt ,JWTError
from datetime import datetime, timedelta 

SECRET_KEY="mysecretkey"
ALGORITHM="HS256"


def hash_password(password:str)->str: 
    password_bytes=password.encode("utf-8")
    salt=bcrypt.gensalt()
    hash_password1=bcrypt.hashpw(password_bytes,salt)
    return hash_password1.decode("utf-8")

def verify_password(plain_password:str,hashed_password:str)->bool:
    plain_password_bytes=plain_password.encode("utf-8")
    hashed_password_bytes=hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_password_bytes,hashed_password_bytes)


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=30)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_token(token:str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        print("Token verification failed",e)
        return None
# password = "mypasssword123"
# hashed = hash_password(password)
# print("stored password:",hashed)
# login_password = "mypasssword123"
# if verify_password(login_password,hashed):
#     print("Login successful")
# else:
#     print("Invalid password")