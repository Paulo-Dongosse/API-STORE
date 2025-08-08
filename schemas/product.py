from pydantic import BaseModel, Field
from models.product import ProductModel

from uuid import UUID, uuid4
from typing import Optional


class ProductIn(BaseModel):
    nome: str = Field(..., min_length=1)
    preco: float
    quantidade: int


class ProductOut(ProductIn):
    id: UUID


class ProductUpdate(BaseModel):
    nome: Optional[str] = None
    preco: Optional[float] = None
    quantidade: Optional[int] = None


class ProductUpdateOut(ProductOut):
    pass
