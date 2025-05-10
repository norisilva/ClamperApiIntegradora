class Produto:
    def __init__(self, codigo: str, descricao: str, nome, fabricante, ano):
        self._codigo = codigo
        self._descricao = descricao
        self._nome = nome
        self._fabricante = fabricante
        self._ano = ano

    @property
    def codigo(self):
        return self._codigo

    @property
    def descricao(self):
        return self._descricao

    @property
    def nome(self):
        return self._nome.valor

    @property
    def fabricante(self):
        return self._fabricante.valor

    @property
    def ano(self):
        return self._ano.valor