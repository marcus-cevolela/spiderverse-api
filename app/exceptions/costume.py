class CostumeNotFoundError(Exception):
    def __init__(self, movie_id: int):
        super().__init__(f"Traje com ID {movie_id} não encontrado.")