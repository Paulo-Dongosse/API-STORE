from fastapi import APIRouter, status
from uuid import UUID
from typing import List

from schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from usecases.product import product_usecase

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def criar_produto(product: ProductIn):
    return await product_usecase.create(product)


@router.get("/", response_model=List[ProductOut])
async def listar():
    return await product_usecase.query()


@router.get("/{id}", response_model=ProductOut)
async def listar_produto_pelo_id(id: UUID):
    return await product_usecase.get(id)


@router.patch("/{id}", response_model=ProductUpdateOut)
async def atualizar_produto_pelo_id(id: UUID, product: ProductUpdate):
    return await product_usecase.update(id, product)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_pelo_id(id: UUID):
    await product_usecase.delete(id)
    
