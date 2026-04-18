from fastapi import FastAPI, HTTPException,Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from schemas import UserRegister , UserLogin
from security import hash_password,verify_password,create_access_token,verify_token

app=FastAPI()
users=[]
security=HTTPBearer()

def get_current_user(credentials:HTTPAuthorizationCredentials=Depends(security)):
    try:
        token=credentials.credentials
        payload=verify_token(token)
    
        if payload is None:
            raise HTTPException(status_code=401,detail="Invalid token")
        return payload
    except Exception as e:
        print("Token verification failed",e)
        raise HTTPException(status_code=401,detail="Could not validate credentials")

@app.post('/register')
def register(user:UserRegister): 
    hashed_password=hash_password(user.password)
    new_user={
        "username":user.username,
        "email":user.email,
        "password":hashed_password
    }
    users.append(new_user)
    return {"message":"User registered successfully"}
@app.post('/login')
def login(user:UserLogin):
    db_user=None
    for u in users:
        if u["email"]==user.email:
            db_user=u
            break            
    
    if db_user is None:
        raise HTTPException(status_code=404,detail='User not found')
    
    if not verify_password(user.password,db_user["password"]):
        raise HTTPException(status_code=401,detail='Incorrect password') 

    token=create_access_token(
                    {"sub":db_user["email"]}
                    )
    return {"access_token":token,
                        "token_type":"bearer"}

@app.get("/profile")   
def profile(user=Depends(get_current_user)):
    if user is None:
        raise HTTPException(status_code=401,detail="Invalid authentication credential")
    return {
        "message":"This is a protected route",
        "user_email":user.get("sub")
    }