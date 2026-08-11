class MovieNotFoundError(Exception):
    def __init__(self, movie_id: int):
        super().__init__(f"Filme com ID {movie_id} não encontrado.")