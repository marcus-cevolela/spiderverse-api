from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text
from app.models.spider_movie import spider_movie
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.costume import Costume
    from app.models.movie import Movie

class Spider(Base):
    __tablename__ = "spiders"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    secret_identity: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(Text())
    thumbnail: Mapped[str] = mapped_column()
    thumbnail_hover: Mapped[str] = mapped_column()
    banner: Mapped[str] = mapped_column()
    slug: Mapped[str] = mapped_column(unique=True)
    suits: Mapped[list["Costume"]] = relationship(back_populates="spider")
    movies: Mapped[list["Movie"]] = relationship(secondary=spider_movie, back_populates="spiders")