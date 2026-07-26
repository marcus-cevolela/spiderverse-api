from fastapi import APIRouter

router = APIRouter(prefix="/spiders")

spiders = {
        1: {
            "id": 1,
            "name": "Spider-Man - TOBEY",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "...",
            "banner": "...",
            "slug": "spider-man"
        },
        2: {
            "id": 2,
            "name": "Spider-Man - ANDREW",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "...",
            "banner": "...",
            "slug": "spider-man"
        },
        3: {
            "id": 3,
            "name": "Spider-Man - TOM",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "...",
            "banner": "...",
            "slug": "spider-man"
        },
    }

@router.get("/")
def get_spiders():
    return spiders

@router.get("/{id_spider}")
def get_spider_by_id(id_spider: int):
    return spiders[id_spider]
