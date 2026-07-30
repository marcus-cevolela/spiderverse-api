from enum import Enum

class SpiderSort(str, Enum):
    id = "id"
    name = "name"
    slug = "slug"
    secret_identity = "secret_identity"

    desc_id = "-id"
    desc_name = "-name"
    desc_slug = "-slug"
    desc_secret_identity = "-secret_identity"