from fastapi import APIRouter, HTTPException, status, Depends, Query
from app.schemas.movie import Movie, MovieCreate, MovieUpdate
from app.services import movies as movie_service
from app.exceptions.movie import MovieNotFoundError
from sqlalchemy.orm import Session
from app.database.connection import get_db

router = APIRouter(prefix="/movies")

@router.get("/", response_model=list[Movie])
def get_movies(
    title_movie: str | None = None,
    db: Session = Depends(get_db),
    limit: int = Query(default=10, gt=0),
    offset: int = Query(default=0, ge=0)
    ):
    return movie_service.get_movies(
        db=db,
        title_movie=title_movie,
        limit=limit,
        offset=offset
    )

@router.get("/{id_movie}", response_model=Movie)
def get_movie_by_id(
    id_movie: int, 
    db: Session = Depends(get_db)
):
    try:
        return movie_service.get_movie_by_id(db, id_movie)
    except MovieNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.post("/", response_model=Movie, status_code=status.HTTP_201_CREATED)
def create_movie(
    movie: MovieCreate,
    db: Session = Depends(get_db),
):
    return movie_service.create_movie(
        db=db,
        movie=movie
    )

@router.put("/{id_movie}", response_model=Movie)
def change_movie_by_id(
    id_movie: int, 
    changed_movie: MovieCreate,
    db: Session = Depends(get_db)
):
    try:
        return movie_service.change_movie_by_id(
            db=db,
            id_movie=id_movie,
            changed_movie=changed_movie
        )
    except MovieNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
    )

@router.delete("/{id_movie}", status_code=status.HTTP_200_OK)
def delete_movie(
    id_movie: int,
    db: Session = Depends(get_db)
):
    try:
        return movie_service.delete_movie(
            db=db,
            id_movie=id_movie
        )
    except MovieNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.patch("/{id_movie}", response_model=Movie)
def update_movie(
    id_movie: int,
    updated_movie: MovieUpdate,
    db: Session = Depends(get_db)
):
    try:
        return movie_service.update_movie(
            db=db,
            id_movie=id_movie,
            updated_movie=updated_movie
        )
    except MovieNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
    )