class Ano:
    def __init__(self, valor: int):
        if valor < 1900 or valor > 2500:
            raise ValueError("O ano deve estar entre 1900 e 2500.")
        self._valor = valor

    @property
    def valor(self):
        return self._valor