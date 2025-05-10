class Fabricante:
    def __init__(self, valor: str):
        if not valor or len(valor.strip()) < 2:
            raise ValueError("O fabricante deve ter pelo menos 2 caracteres.")
        self._valor = valor.strip()

    @property
    def valor(self):
        return self._valor