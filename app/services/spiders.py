
from sqlalchemy.orm import Session
from sqlalchemy import select
# from app.data.spiders import spiders
from app.models.spider import Spider as SpiderModel
from app.exceptions.spider import SpiderNotFoundError
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

def get_spider_by_id(db: Session,id_spider: int):
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