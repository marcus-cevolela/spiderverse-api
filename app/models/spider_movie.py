from sqlalchemy import Table, Column, ForeignKey, Integer
from app.database.base import Base

spider_movie = Table(
    "spider_movies",
    Base.metadata,
    Column ("spider_id", Integer, ForeignKey("spiders.id"), primary_key=True),
    Column ("movie_id", Integer, ForeignKey("movies.id"), primary_key=True)
)