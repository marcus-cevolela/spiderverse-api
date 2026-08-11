from app.routers.spiders import router as spider_router
from app.routers.movies import router as movie_router

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine
import app.models.spider
import app.models.movie
import app.models.costume
import app.models.spider_movie

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

app.include_router(spider_router, prefix="/api/v1")

app.include_router(movie_router, prefix="/api/v1")
