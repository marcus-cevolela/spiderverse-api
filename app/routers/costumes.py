from fastapi import APIRouter, HTTPException, status, Depends, Query
from app.schemas.costume import Costume, CostumeCreate, CostumeUpdate
from app.schemas.spider import Spider
from app.services import costumes as costume_service
from app.exceptions.costume import CostumeNotFoundError
from sqlalchemy.orm import Session
from app.database.connection import get_db

router = APIRouter(
    prefix="/costumes",
    tags=["Costumes"]
)

@router.get("/", response_model=list[Costume])
def get_costumes(
    name_costume: str | None = None,
    db: Session = Depends(get_db),
    limit: int = Query(default=10, gt=0),
    offset: int = Query(default=0, ge=0)
):
    return costume_service.get_costumes(
        db=db,
        name_costume=name_costume,
        limit=limit,
        offset=offset
    )

@router.get("/{id_costume}", response_model=Costume)
def get_costume_by_id(
    id_costume: int,
    db: Session = Depends(get_db)
):
    try:
        return costume_service.get_costume_by_id(db, id_costume)
    except CostumeNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("/", response_model=Costume, status_code=status.HTTP_201_CREATED)
def create_costume(
    costume: CostumeCreate,
    db: Session = Depends(get_db),
):
    return costume_service.create_costume(
        db=db,
        costume=costume
    )

@router.put("/{id_costume}", response_model=Costume)
def change_costume_by_id(
    id_costume: int, 
    changed_costume: CostumeCreate,
    db: Session = Depends(get_db)
):
    try:
        return costume_service.change_costume_by_id(
            db=db,
            id_costume=id_costume,
            changed_costume=changed_costume
        )
    except CostumeNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
    )

@router.delete("/{id_costume}", status_code=status.HTTP_200_OK)
def delete_costume(
    id_costume: int,
    db: Session = Depends(get_db)
):
    try:
        return costume_service.delete_costume(
            db=db,
            id_costume=id_costume
        )
    except CostumeNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.patch("/{id_costume}", response_model=Costume)
def update_costume(
    id_costume: int,
    updated_costume: CostumeUpdate,
    db: Session = Depends(get_db)
):
    try:
        return costume_service.update_costume(
            db=db,
            id_costume=id_costume,
            updated_costume=updated_costume
        )
    except CostumeNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.get("/{costume_id}/spiders", response_model=list[Spider])
def get_spiders_by_costume(
    costume_id: int,
    db: Session = Depends(get_db)
):
    try:
        return costume_service.get_spiders_by_costume(
            db=db,
            costume_id=costume_id,
        )
    except CostumeNotFoundError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
        )