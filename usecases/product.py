from typing import List
from uuid import UUID
from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorDatabase
import pymongo

from db.mongo import db_client
from models.product import ProductModel
from schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from core.exceptions import NotFoundException


class ProductUsecase:
    def __init__(self) -> None:
        self.database: AsyncIOMotorDatabase = db_client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, corpo: ProductIn) -> ProductOut:
        
        produto_dict  = corpo.model_dump()
        produto_dict["id"] = str(produto_dict .get("id", uuid4()))
        await self.collection.insert_one(produto_dict )
        return ProductOut(**produto_dict )

    async def get(self, id: UUID) -> ProductOut:
        # Busca pelo id como string
        resultado = await self.collection.find_one({"id": str(id)})
        if not resultado:
            raise NotFoundException(messagem=f"Produto não encontrado com o id: {id}")

        # Converte o id de volta para UUID para o schema
        resultado["id"] = UUID(resultado["id"])
        return ProductOut(**resultado)

    async def query(self) -> List[ProductOut]:
        products = []
        async for item in self.collection.find():
            item["id"] = UUID(item["id"])  # converter string para UUID
            products.append(ProductOut(**item))
        return products

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        atualizar_dados = body.model_dump(exclude_none=True)
        resultado = await self.collection.find_one_and_update(
            filter={"id": str(id)},
            update={"$set": atualizar_dados},
            return_document=pymongo.ReturnDocument.AFTER,
        )
        if not resultado:
            raise NotFoundException(messagem=f"Produto não encontrado com o id: {id}")

        resultado["id"] = UUID(resultado["id"])
        return ProductUpdateOut(**resultado)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": str(id)})
        if not product:
            raise NotFoundException(messagem=f"Produto não encontrado com o id: {id}")
        result = await self.collection.delete_one({"id": str(id)})
        return result.deleted_count > 0


product_usecase = ProductUsecase()
