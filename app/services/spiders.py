from app.enums.spider import SpiderSort
from app.data.spiders import spiders
from app.exceptions.spider import SpiderNotFoundError
from app.schemas.spider import SpiderCreate, SpiderUpdate

def get_spiders(
    name_spider: str | None = None,
    slug_spider: str | None = None,
    sort: SpiderSort | None = None,
    limit: int = 10,
    offset: int = 0):
    
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

def get_spider_by_id(
    id_spider: int
):
    for spider in spiders:
        if spider["id"] == id_spider:
            return spider

    raise SpiderNotFoundError(id_spider)

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