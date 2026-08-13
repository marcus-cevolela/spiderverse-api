class ExistentRelationshipError(Exception):
    def __init__(self, spider_id: int, movie_id: int):
        super().__init__(f"A relação entre Spider {spider_id} e Filme {movie_id} já existe.")

class NonExistentRelationshipError(Exception):
    def __init__(self, spider_id: int, movie_id: int):
        super().__init__(f"Não existe nenhuma relação entre Spider {spider_id} e Filme {movie_id}.")