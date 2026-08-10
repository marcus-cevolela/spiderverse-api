from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text
from datetime import date
from app.models.spider_movie import spider_movie
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.costume import Costume
    from app.models.spider import Spider

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(Text())
    release_date: Mapped[date] = mapped_column()
    poster: Mapped[str] = mapped_column()
    costumes: Mapped[list["Costume"]] = relationship(back_populates="first_appearance_movie")
    spiders: Mapped[list["Spider"]] = relationship(secondary=spider_movie, back_populates="movies")