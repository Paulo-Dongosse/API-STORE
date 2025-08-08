from fastapi import FastAPI
from routes import product

app = FastAPI(
    title="API TDD Store",
    version="1.0.0",
    description="API de gerenciamento de produtos usando FastAPI, MongoDB e TDD."
)

# Inclui as rotas do módulo product
app.include_router(product.router)
