from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.spider import Spider, SpiderCreate, SpiderUpdate
from app.services import spiders as spider_service
from app.exceptions.spider import SpiderNotFoundError
from sqlalchemy.orm import Session
from app.database.connection import get_db

router = APIRouter(prefix="/spiders")

@router.get("/", response_model=list[Spider])
def get_spiders(db: Session = Depends(get_db)):
    return spider_service.get_spiders(db)

@router.get("/{id_spider}", response_model=Spider)
def get_spider_by_id(id_spider: int, db: Session = Depends(get_db)):
    try:
        return spider_service.get_spider_by_id(db, id_spider)
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


