from pydantic import BaseModel, Field, HttpUrl
from datetime import date

class MovieBase(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    release_date: date
    poster: HttpUrl

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

class MovieUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = Field(None, min_length=1)
    release_date: date | None = None
    poster: HttpUrl | None = None