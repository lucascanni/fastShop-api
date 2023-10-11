from pydantic import BaseModel
import uuid

# Model Pydantic = Datatype
class Product(BaseModel):
    id: str
    category: str
    name: str
    price: float
    description: str 