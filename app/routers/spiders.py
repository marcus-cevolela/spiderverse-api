from fastapi import APIRouter, HTTPException, status, Query
from app.schemas.spider import Spider, SpiderCreate, SpiderUpdate
from app.enums.spider import SpiderSort

router = APIRouter(prefix="/spiders")

spiders = [
        {
            "id": 1,
            "name": "cSpider-Man",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "https://example.com/",
            "banner": "https://example.com/",
            "slug": "tobey-maguire"
        },
        {
            "id": 2,
            "name": "aSpider-Man",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "https://example.com/",
            "banner": "https://example.com/",
            "slug": "andrew-garfield"
        },
        {
            "id": 3,
            "name": "bTOM HOLLAND",
            "secretIdentity": "Peter Parker",
            "description": "...",
            "thumbnail": "https://example.com/",
            "banner": "https://example.com/",
            "slug": "tom-holland"
        },
    ]

@router.get("/", response_model=list[Spider])
def get_spiders(
    name_spider: str | None = Query(
        default=None,
        min_length=3,
        description="Filtra personagens pelo nome.",
        example="Spider-Man"),
    slug_spider: str | None =  Query(
        default=None,
        min_length=3,
        description="Filtra personagens pelo slug.",
        example="tobey-maguire"),
    sort: SpiderSort | None = Query(
        default=None,
        description="Campo utilizado para ordenar os personagens.",
        example="name"),
    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Quantidade máxima de personagens retornados."),
    offset: int = Query(
        default=0,
        ge=0,
        description="Quantidade de personagens a serem ignorados.")):

    reverse = False
    
    if name_spider is None and slug_spider is None and sort is None:
        return spiders[offset:offset+limit]

    result_spiders = []
    for spider in spiders:
        if name_spider is not None:
            if spider["name"].lower() != name_spider.lower():
                continue

        if slug_spider is not None:
            if spider["slug"].lower() != slug_spider.lower():
                continue

        result_spiders.append(spider)

    if sort is not None:
        sort_key = sort.value
        if sort_key.startswith("-"):
            reverse = True
            sort_key = sort_key[1:]
        
        result_spiders = sorted(
            result_spiders, 
            key=lambda spider: spider[sort_key],
            reverse=reverse)

    return result_spiders[offset:offset+limit]


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


