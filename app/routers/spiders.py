from fastapi import APIRouter, HTTPException, status, Query
from app.schemas.spider import Spider, SpiderCreate, SpiderUpdate
from app.enums.spider import SpiderSort
from app.services import spiders as spider_service
from app.exceptions.spider import SpiderNotFoundError

router = APIRouter(prefix="/spiders")

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
        description="Quantidade de personagens a serem ignorados.")
):
    return spider_service.get_spiders(
        name_spider=name_spider,
        slug_spider=slug_spider,
        sort=sort,
        limit=limit,
        offset=offset,
    )

@router.get("/{id_spider}", response_model=Spider)
def get_spider_by_id(id_spider: int):
    try:
        return spider_service.get_spider_by_id(id_spider)
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("/", response_model=Spider, status_code=status.HTTP_201_CREATED)
def create_spider(spider: SpiderCreate):
    return spider_service.create_spider(spider)

@router.put("/{id_spider}", response_model=Spider)
def change_spider_by_id(id_spider: int, changed_spider: SpiderCreate):
    try:
        return spider_service.change_spider_by_id(id_spider, changed_spider)
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
    )

@router.delete("/{id_spider}", status_code=status.HTTP_200_OK)
def delete_spider(id_spider: int):
    try:
        return spider_service.delete_spider(id_spider)
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.patch("/{id_spider}")
def update_spider(id_spider: int, updated_spider: SpiderUpdate):
    try:
        return spider_service.update_spider(id_spider, updated_spider)
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
    )


