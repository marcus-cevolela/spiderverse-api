from app.routers.spiders import router

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine
import app.models.spider

API_TITLE = "SpiderVerse API"
API_DESCRIPTION = '''🇧🇷 API REST sobre o universo do Homem-Aranha.
🇺🇸 REST API about the Spider-Man universe.'''
API_VERSION = "1.0.0"

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=API_TITLE, 
    description=API_DESCRIPTION, 
    version=API_VERSION,
    lifespan=lifespan
    )

@app.get("/")
def api_info():
    return {
        "title": API_TITLE,
        "description": API_DESCRIPTION,
        "version": API_VERSION
        }

app.include_router(router, prefix="/api/v1")
