from fastapi import APIRouter, HTTPException, status
from app.schemas.spider import Spider, SpiderCreate

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

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Spider não encontrado.")

@router.post("/", response_model=Spider, status_code=status.HTTP_201_CREATED)
def create_spider(spider: SpiderCreate):
    new_id = len(spiders) + 1
    dados = spider.model_dump()
    dados["id"] = new_id
    spiders.append(dados)
    return dados

@router.put("/{id_spider}", response_model=Spider)
def change_spider_by_id(id_spider: int, changed_spider: SpiderCreate):
    for indice, spider in enumerate(spiders):
        if spider["id"] == id_spider:
            dados = changed_spider.model_dump()
            dados["id"] = id_spider
            spiders[indice] = dados
            return dados

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Spider não encontrado.")






