from pydantic import BaseModel

# Model Pydantic = Datatype
class Product(BaseModel):
    id: str
    category: str
    name: str
    price: float
    description: str 

class User(BaseModel):
    email: str
    password: str
