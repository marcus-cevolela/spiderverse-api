from fastapi import FastAPI
from app.routers.spiders import router

API_TITLE = "SpiderVerse API"
API_DESCRIPTION = '''🇧🇷 API REST sobre o universo do Homem-Aranha.
🇺🇸 REST API about the Spider-Man universe.'''
API_VERSION = "1.0.0"

app = FastAPI(
    title=API_TITLE, 
    description=API_DESCRIPTION, 
    version=API_VERSION
    )

@app.get("/")
def api_info():
    return {
        "title": API_TITLE,
        "description": API_DESCRIPTION,
        "version": API_VERSION
        }

app.include_router(router, prefix="/api/v1")


