from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text

class Spider(Base):
    __tablename__ = "spiders"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    secret_identity: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(Text())
    thumbnail: Mapped[str] = mapped_column()
    banner: Mapped[str] = mapped_column()
    slug: Mapped[str] = mapped_column(unique=True)
