from pydantic import BaseModel

class Spider(BaseModel):
    id: int
    name: str
    secretIdentity: str
    description: str
    thumbnail: str
    banner: str
    slug: str

class SpiderCreate(BaseModel):
    name: str
    secretIdentity: str
    description: str
    thumbnail: str
    banner: str
    slug: str
