from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import os


class MongoDBClient:
    def __init__(self, uri: str = None, db_name: str = None):
        self.uri = uri or os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.db_name = db_name or os.getenv("MONGO_DB_NAME", "api_tdd_store")
        self._client: AsyncIOMotorClient = None

    def get(self) -> AsyncIOMotorClient:
        if not self._client:
            self._client = AsyncIOMotorClient(self.uri)
        return self._client

    def get_database(self) -> AsyncIOMotorDatabase:
        return self.get()[self.db_name]
    



db_client = MongoDBClient()
