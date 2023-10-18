from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post("/signup", status_code=201)
async def createAccount():
    return {"message": "signup"}

@router.post("/login")
async def createSwaggerToken():
    return {"message": "login"}

@router.get("/me")
def secure_endpoint():
    return {"message": "me"}