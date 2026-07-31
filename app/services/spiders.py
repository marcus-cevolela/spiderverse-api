
from sqlalchemy.orm import Session
from sqlalchemy import select
# from app.data.spiders import spiders
from app.models.spider import Spider
from app.exceptions.spider import SpiderNotFoundError
from app.schemas.spider import SpiderCreate, SpiderUpdate

def get_spiders(
        db: Session, 
        name_spider: str | None = None,
        slug_spider: str | None= None,
        limit: int = 10,
        offset: int = 0
): 
    
    consulta = select(Spider)

    if name_spider is not None:
        consulta = consulta.where(Spider.name == name_spider)

    if slug_spider is not None:
            consulta = consulta.where(Spider.slug == slug_spider)

    consulta = consulta.limit(limit).offset(offset)

    result = db.execute(consulta) 
    return result.scalars().all()

def get_spider_by_id(db: Session,id_spider: int):
    result = db.execute(
        select(Spider).where(Spider.id == id_spider)
    )

    spider = result.scalars().first()

    if spider is None:
        raise SpiderNotFoundError(id_spider)

    return spider

def create_spider(
    spider: SpiderCreate
):
    new_id = len(spiders) + 1
    dados = spider.model_dump()
    dados["id"] = new_id
    spiders.append(dados)
    return dados

def change_spider_by_id(
    id_spider: int, 
    changed_spider: SpiderCreate
):
    for indice, spider in enumerate(spiders):
        if spider["id"] == id_spider:
            dados = changed_spider.model_dump()
            dados["id"] = id_spider
            spiders[indice] = dados
            return dados

    raise SpiderNotFoundError(id_spider)

def delete_spider(
    id_spider: int
):
    for indice, spider in enumerate(spiders):
        if spider["id"] == id_spider:
            spiders.pop(indice)
            return {"message": "Spider removido com sucesso."}

    raise SpiderNotFoundError(id_spider)

def update_spider(id_spider: int, updated_spider: SpiderUpdate):
    for spider in spiders:
        if spider["id"] == id_spider:
            campos_atualizados = updated_spider.model_dump(exclude_unset=True)
            spider.update(campos_atualizados)
            return spider

    raise SpiderNotFoundError(id_spider)