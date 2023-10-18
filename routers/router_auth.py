from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from classes.schemas_dto import User
from database.firebase import authProduct
from firebase_admin import auth

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post("/signup", status_code=201)
async def createAccount(user_body:User):
    try:
        user = auth.create_user(
            email=user_body.email,
            password=user_body.password,
        )
        return {"message": f"New user created successfully"}
    except auth.authentication.UserNotFoundError:
        raise HTTPException(
            status_code=400, detail=f"User already exists"
        )

@router.post("/login")
async def createSwaggerToken(user_credentials: OAuth2PasswordRequestForm = Depends()):
    try:
        print(user_credentials)
        user = authProduct.sign_in_with_email_and_password(user_credentials.username, 
                                                           user_credentials.password)
        token = user['idToken']
        print(token)
        return {"access_token": token,
                "token_type": "bearer"}
    except auth.authentication.InvalidPasswordError:
        raise HTTPException(
            status_code=401, detail=f"Invalid password"
        )
    except auth.authentication.UserNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"User not found"
        )
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
def get_current_user(provided_token: str = Depends(oauth2_scheme)):
    decoded_token = auth.verify_id_token(provided_token)
    decoded_token['idToken'] = provided_token
    return decoded_token

@router.get("/me")
def secure_endpoint(userData: int = Depends(get_current_user)):
    return userData