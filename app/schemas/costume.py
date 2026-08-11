from pydantic import BaseModel, Field, HttpUrl

class CostumeBase(BaseModel):
    name: str = Field(min_length=1)
    movie_id: int
    thumbnail: HttpUrl
    model_3d: HttpUrl
    spider_id: int

class CostumeCreate(CostumeBase):
    pass

class Costume(CostumeBase):
    id: int

class CostumeUpdate(BaseModel):
    name: str | None = Field(None, min_length=1)
    movie_id: int | None = None
    thumbnail: HttpUrl | None = None
    model_3d: HttpUrl | None = None
    spider_id: int | None = None