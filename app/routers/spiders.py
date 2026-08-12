from fastapi import APIRouter, HTTPException, status, Depends, Query
from app.schemas.spider import Spider, SpiderCreate, SpiderUpdate
from app.services import spiders as spider_service
from app.exceptions.spider import SpiderNotFoundError
from app.exceptions.movie import MovieNotFoundError
from app.exceptions.spider_movie import ExistentRelationshipError
from sqlalchemy.orm import Session
from app.database.connection import get_db

router = APIRouter(
    prefix="/spiders",
    tags=["Spiders"]
)

@router.get("/", response_model=list[Spider])
def get_spiders(
    name_spider: str | None = None,
    slug_spider: str | None = None,
    db: Session = Depends(get_db),
    limit: int = Query(default=10, gt=0),
    offset: int = Query(default=0, ge=0)
    ):
    return spider_service.get_spiders(
        db=db,
        name_spider=name_spider,
        slug_spider=slug_spider,
        limit=limit,
        offset=offset
    )

@router.get("/{id_spider}", response_model=Spider)
def get_spider_by_id(
    id_spider: int, 
    db: Session = Depends(get_db)
):
    try:
        return spider_service.get_spider_by_id(db, id_spider)
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("/", response_model=Spider, status_code=status.HTTP_201_CREATED)
def create_spider(
    spider: SpiderCreate,
    db: Session = Depends(get_db),
):
    return spider_service.create_spider(
        db=db,
        spider=spider
    )

@router.put("/{id_spider}", response_model=Spider)
def change_spider_by_id(
    id_spider: int, 
    changed_spider: SpiderCreate,
    db: Session = Depends(get_db)
):
    try:
        return spider_service.change_spider_by_id(
            db=db,
            id_spider=id_spider,
            changed_spider=changed_spider
        )
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
    )

@router.delete("/{id_spider}", status_code=status.HTTP_200_OK)
def delete_spider(
    id_spider: int,
    db: Session = Depends(get_db)
):
    try:
        return spider_service.delete_spider(
            db=db,
            id_spider=id_spider
        )
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.patch("/{id_spider}", response_model=Spider)
def update_spider(
    id_spider: int, 
    updated_spider: SpiderUpdate,
    db: Session = Depends(get_db)
):
    try:
        return spider_service.update_spider(
            db=db,
            id_spider=id_spider,
            updated_spider=updated_spider
        )
    except SpiderNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
    )

@router.post("/{spider_id}/movies/{movie_id}",status_code=status.HTTP_201_CREATED)
def add_movie_to_spider(
    spider_id: int,
    movie_id: int,
    db: Session = Depends(get_db)
):
    try:
        return spider_service.add_movie_to_spider(
            db=db,
            spider_id=spider_id,
            movie_id=movie_id
        )
    except SpiderNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
        )
    except MovieNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
        )
    except ExistentRelationshipError as e:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=str(e)
        )

