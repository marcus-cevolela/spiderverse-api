class ExistentRelationshipError(Exception):
    def __init__(self, first_id: int, second_id: int):
        super().__init__(f"A relação entre os registros {first_id} e {second_id} já existe.")

class NonExistentRelationshipError(Exception):
    def __init__(self, first_id: int, second_id: int):
        super().__init__(f"Não existe nenhuma relação entre os registros {first_id} e {second_id}.")