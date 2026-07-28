class SpiderNotFoundError(Exception):
    def __init__(self, spider_id: int):
        super().__init__(f"Spider com ID {spider_id} não encontrado.")