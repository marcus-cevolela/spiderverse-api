from sqlalchemy import Table, Column, ForeignKey, Integer
from app.database.base import Base

spider_costume = Table(
    "spider_costumes",
    Base.metadata,
    Column("spider_id", Integer, ForeignKey("spiders.id"), primary_key=True),
    Column("costume_id", Integer, ForeignKey("costumes.id"), primary_key=True)
)