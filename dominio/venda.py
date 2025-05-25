class Venda:
    def __init__(self, codigo: str, comprador: str, quantidade, valor, codigo_produto):
        self._codigo = codigo
        self._comprador = comprador
        self._quantidade = quantidade
        self._valor = valor
        self._codigo_produto = codigo_produto
        self._data_recepcao = None
        self._uui_recepcao = None
        self._status_recepcao = None

    @property
    def codigo(self):
        return self._codigo

    @property
    def comprador(self):
        return self._comprador

    @property
    def quantidade(self):
        return self._quantidade.valor

    @property
    def valor(self):
        return self._valor.valor

    @property
    def codigo_produto(self):
        return self._codigo_produto.valor

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