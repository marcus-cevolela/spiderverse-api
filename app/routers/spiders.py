from fastapi import APIRouter, HTTPException, status
from app.schemas.spider import Spider, SpiderCreate, SpiderUpdate

router = APIRouter(prefix="/spiders")

spiders = [
        {
            "id": 1,
            "name": "Spider Man",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "https://example.com/",
            "banner": "https://example.com/",
            "slug": "tobey-maguire"
        },
        {
            "id": 2,
            "name": "Spider Man",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "https://example.com/",
            "banner": "https://example.com/",
            "slug": "andrew-garfield"
        },
        {
            "id": 3,
            "name": "TOM HOLLAND",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "https://example.com/",
            "banner": "https://example.com/",
            "slug": "tom-holland"
        },
    ]

@router.get("/", response_model=list[Spider])
def get_spiders(name_spider: str | None = None):
    if name_spider is None:
        return spiders

    filtered_spiders = []
    for spider in spiders:
        if spider["name"].lower() == name_spider.lower():
            filtered_spiders.append(spider)

    return filtered_spiders
        


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

@router.delete("/{id_spider}", status_code=status.HTTP_200_OK)
def delete_spider(id_spider: int):
    for indice, spider in enumerate(spiders):
            if spider["id"] == id_spider:
                spiders.pop(indice)
                return {"message": "Spider removido com sucesso."}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Spider não encontrado.")

@router.patch("/{id_spider}")
def update_spider(id_spider: int, updated_spider: SpiderUpdate):
    for spider in spiders:
        if spider["id"] == id_spider:
            campos_atualizados = updated_spider.model_dump(exclude_unset=True)
            spider.update(campos_atualizados)
            return spider

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Spider não encontrado.")
