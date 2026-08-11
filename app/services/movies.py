from sqlalchemy.orm import Session
from sqlalchemy import select
# from app.data.spiders import spiders
from app.models.movie import Movie as MovieModel
from app.exceptions.movie import MovieNotFoundError
from app.schemas.movie import MovieCreate, MovieUpdate

def get_movies(
    db: Session,
    title_movie: str | None = None,
    limit: int = 10,
    offset: int = 0
):
    consulta = select(MovieModel)

    if title_movie is not None:
        consulta = consulta.where(MovieModel.title == title_movie)

    consulta = consulta.order_by(MovieModel.id)
    consulta = consulta.limit(limit).offset(offset)

    result = db.execute(consulta)
    return result.scalars().all()

def get_movie_by_id(
    db: Session,
    id_movie: int
):
    result = db.execute(
        select(MovieModel).where(MovieModel.id == id_movie)
    )

    movie = result.scalars().first()

    if movie is None:
        raise MovieNotFoundError(id_movie)

    return movie

def create_movie(
    db: Session,
    movie: MovieCreate
):
    novo_movie = MovieModel(**movie.model_dump(mode="json"))
    db.add(novo_movie)
    db.commit()
    db.refresh(novo_movie)
    return novo_movie

def change_movie_by_id(
    db: Session,
    id_movie: int,
    changed_movie: MovieCreate
):
    movie = get_movie_by_id(db, id_movie)

    dados = changed_movie.model_dump(mode="json")

    for chave, valor in dados.items():
        setattr(movie, chave, valor)

    db.commit()
    db.refresh(movie)
    
    return movie

def delete_movie(
    db: Session,
    id_movie: int
):
    movie = get_movie_by_id(db, id_movie)

    db.delete(movie)
    db.commit()

    return {
        "message": "Filme removido com sucesso."
    }

def update_movie(
    db: Session,
    id_movie: int,
    updated_movie: MovieUpdate
):
    movie = get_movie_by_id(db, id_movie)

    dados = updated_movie.model_dump(mode="json", exclude_unset=True)

    for chave, valor in dados.items():
        setattr(movie, chave, valor)

    db.commit()
    db.refresh(movie)
            
    return movie