from fastapi import APIRouter, HTTPException
from app.schemas.spider import Spider

router = APIRouter(prefix="/spiders")

spiders = [
        {
            "id": 1,
            "name": "Spider-Man - TOBEY",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "...",
            "banner": "...",
            "slug": "spider-man"
        },
        {
            "id": 2,
            "name": "Spider-Man - ANDREW",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "...",
            "banner": "...",
            "slug": "spider-man"
        },
        {
            "id": 3,
            "name": "Spider-Man - TOM",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "...",
            "banner": "...",
            "slug": "spider-man"
        },
    ]

@router.get("/", response_model=list[Spider])
def get_spiders():
    return spiders

@router.get("/{id_spider}", response_model=Spider)
def get_spider_by_id(id_spider: int):
    for spider in spiders:
        if spider["id"] == id_spider:
            return spider

    raise HTTPException(status_code=404, detail="Spider não encontrado.")


