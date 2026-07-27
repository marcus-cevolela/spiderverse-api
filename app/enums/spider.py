from enum import Enum

class SpiderSort(str, Enum):
    id = "id"
    name = "name"
    slug = "slug"
    secretIdentity = "secretIdentity"

    desc_id = "-id"
    desc_name = "-name"
    desc_slug = "-slug"
    desc_secretIdentity = "-secretIdentity"