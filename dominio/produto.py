class Produto:
    def __init__(self, codigo: str, descricao: str, nome, fabricante, ano):
        self._codigo = codigo
        self._descricao = descricao
        self._nome = nome
        self._fabricante = fabricante
        self._ano = ano
        self._data_recepcao = None
        self._uui_recepcao = None
        self._status_recepcao = None

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

    @property
    def data_recepcao(self):
        return self._data_recepcao

    @data_recepcao.setter
    def data_recepcao(self, value):
        self._data_recepcao = value

    @property
    def uui_recepcao(self):
        return self._uui_recepcao

    @uui_recepcao.setter
    def uui_recepcao(self, value):
        self._uui_recepcao = value

    @property
    def status_recepcao(self):
        return self._status_recepcao

    @status_recepcao.setter
    def status_recepcao(self, value):
        self._status_recepcao = value