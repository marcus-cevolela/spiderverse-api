from sqlalchemy.orm import Session
from sqlalchemy import select, and_, insert
from app.models.spider import Spider as SpiderModel
from app.models.movie import Movie as MovieModel
from app.models.spider_movie import spider_movie as SpiderMovieModel
from app.exceptions.spider import SpiderNotFoundError
from app.exceptions.movie import MovieNotFoundError
from app.exceptions.spider_movie import ExistentRelationshipError
from app.schemas.spider import SpiderCreate, SpiderUpdate


def get_spiders(
        db: Session, 
        name_spider: str | None = None,
        slug_spider: str | None= None,
        limit: int = 10,
        offset: int = 0
): 
    
    consulta = select(SpiderModel)

    if name_spider is not None:
        consulta = consulta.where(SpiderModel.name == name_spider)

    if slug_spider is not None:
        consulta = consulta.where(SpiderModel.slug == slug_spider)

    consulta = consulta.order_by(SpiderModel.id)
    consulta = consulta.limit(limit).offset(offset)

    result = db.execute(consulta) 
    return result.scalars().all()

def get_spider_by_id(
    db: Session,
    id_spider: int
):
    result = db.execute(
        select(SpiderModel).where(SpiderModel.id == id_spider)
    )

    spider = result.scalars().first()

    if spider is None:
        raise SpiderNotFoundError(id_spider)

    return spider

def create_spider(
    db: Session,
    spider: SpiderCreate
):
    novo_spider = SpiderModel(**spider.model_dump(mode="json"))
    db.add(novo_spider)
    db.commit()
    db.refresh(novo_spider)
    return novo_spider

def change_spider_by_id(
        db: Session,
        id_spider: int,
        changed_spider: SpiderCreate
):
    spider = get_spider_by_id(db, id_spider)

    dados = changed_spider.model_dump(mode="json")

    for chave, valor in dados.items():
        setattr(spider, chave, valor)

    db.commit()
    db.refresh(spider)
    
    return spider

def delete_spider(
    db: Session,
    id_spider: int,
):
    spider = get_spider_by_id(db, id_spider)

    db.delete(spider)
    db.commit()

    return {
        "message": "Spider removido com sucesso."
    }

def update_spider(
        db: Session,
        id_spider: int,
        updated_spider: SpiderUpdate
):
    spider = get_spider_by_id(db, id_spider)

    dados = updated_spider.model_dump(mode="json", exclude_unset=True)

    for chave, valor in dados.items():
        setattr(spider, chave, valor)

    db.commit()
    db.refresh(spider)
            
    return spider

def add_movie_to_spider(
    db: Session,
    spider_id: int,
    movie_id: int
):

    result_spider = db.execute(select(SpiderModel).where(SpiderModel.id == spider_id))
    result_movie = db.execute(select(MovieModel).where(MovieModel.id == movie_id))

    spider = result_spider.scalars().first()
    movie = result_movie.scalars().first()

    if spider is None:
        raise SpiderNotFoundError(spider_id)

    if movie is None:
        raise MovieNotFoundError(movie_id)

    consulta = select(SpiderMovieModel).where(and_(SpiderMovieModel.c.spider_id == spider_id, SpiderMovieModel.c.movie_id == movie_id))
    result = db.execute(consulta)
    relacao = result.first()

    if relacao is not None:
        raise ExistentRelationshipError(spider_id, movie_id)

    consulta_insert = insert(SpiderMovieModel).values(
    spider_id=spider_id,
    movie_id=movie_id
)

    db.execute(consulta_insert)
    db.commit()

    return {
        "message": "Filme associado ao Spider com sucesso."
    }

def get_movies_by_spider(
    db: Session,
    spider_id: int
):
    get_spider_by_id(db, spider_id)

    result = db.execute(select(SpiderMovieModel.c.movie_id).where(SpiderMovieModel.c.spider_id == spider_id))

    movie_ids = result.scalars().all()

    movies = []
    for movie_id in movie_ids:
        result_movie = db.execute(select(MovieModel).where(MovieModel.id == movie_id))
        movie = result_movie.scalars().first()
        movies.append(movie)

    return movies