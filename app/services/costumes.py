from sqlalchemy.orm import Session
from sqlalchemy import select
# from app.data.spiders import spiders
from app.models.costume import Costume as CostumeModel
from app.exceptions.costume import CostumeNotFoundError
from app.schemas.costume import CostumeCreate, CostumeUpdate

def get_costumes(
        db: Session, 
        name_costume: str | None = None,
        limit: int = 10,
        offset: int = 0
): 
    
    consulta = select(CostumeModel)

    if name_costume is not None:
        consulta = consulta.where(CostumeModel.name == name_costume)

    consulta = consulta.order_by(CostumeModel.id)
    consulta = consulta.limit(limit).offset(offset)

    result = db.execute(consulta) 
    return result.scalars().all()

def get_costume_by_id(
    db: Session,
    id_costume: int
):
    result = db.execute(
        select(CostumeModel).where(CostumeModel.id == id_costume)
    )

    costume = result.scalars().first()

    if costume is None:
        raise CostumeNotFoundError(id_costume)

    return costume

def create_costume(
    db: Session,
    costume: CostumeCreate
):
    novo_costume = CostumeModel(**costume.model_dump(mode="json"))
    db.add(novo_costume)
    db.commit()
    db.refresh(novo_costume)
    return novo_costume

def change_costume_by_id(
    db: Session,
    id_costume: int,
    changed_costume: CostumeCreate
):
    costume = get_costume_by_id(db, id_costume)

    dados = changed_costume.model_dump(mode="json")

    for chave, valor in dados.items():
        setattr(costume, chave, valor)

    db.commit()
    db.refresh(costume)
    
    return costume

def delete_costume(
    db: Session,
    id_costume: int
):
    costume = get_costume_by_id(db, id_costume)
    
    db.delete(costume)
    db.commit()
    
    return {
        "message": "Traje removido com sucesso."
    }

def update_costume(
    db: Session,
    id_costume: int,
    updated_costume: CostumeUpdate
):
    costume = get_costume_by_id(db, id_costume)

    dados = updated_costume.model_dump(mode="json", exclude_unset=True)

    for chave, valor in dados.items():
        setattr(costume, chave, valor)

    db.commit()
    db.refresh(costume)
            
    return costume