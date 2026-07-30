from pydantic import BaseModel, Field, HttpUrl

class SpiderBase(BaseModel):
    name: str = Field(min_length=1)
    secret_identity: str = Field(min_length=1)
    description: str = Field(min_length=1)
    thumbnail: HttpUrl
    banner: HttpUrl
    slug: str = Field(min_length=1, pattern="^[a-z0-9-]+$")

class SpiderCreate(SpiderBase):
    pass

class Spider(SpiderBase):
    id: int

class SpiderUpdate(BaseModel):
    name: str | None = Field(None, min_length=1)
    secret_identity: str | None = Field(None, min_length=1)
    description: str | None = Field(None, min_length=1)
    thumbnail: HttpUrl | None = None
    banner: HttpUrl | None = None
    slug: str | None = Field(None, min_length=1, pattern="^[a-z0-9-]+$")