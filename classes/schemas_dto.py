from pydantic import BaseModel
from uuid import UUID

# Model Pydantic = Datatype
class Product(BaseModel):
    id: UUID
    category: str
    sousCategory: str
    name: str
    price: float
    description: str 