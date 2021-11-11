from fastapi import FastAPI
from app import search

app = FastAPI(openapi_url="/search/openapi.json", docs_url="/search/docs", redoc_url="/search/redoc")

app.include_router(search.router)
