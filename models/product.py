from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class ProductModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nome: str
    preco: float
    quantidade: int
