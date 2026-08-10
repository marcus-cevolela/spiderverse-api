from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.spider import Spider
    from app.models.movie import Movie

class Costume(Base):
    __tablename__ = "costumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    first_appearance_movie: Mapped["Movie"] = relationship(back_populates="costumes")
    thumbnail: Mapped[str] = mapped_column()
    model_3d: Mapped[str] = mapped_column()
    spider_id: Mapped[int] = mapped_column(ForeignKey("spiders.id"))
    spider: Mapped["Spider"] = relationship(back_populates="suits")