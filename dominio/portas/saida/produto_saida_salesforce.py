from abc import ABC, abstractmethod
from dominio.produto import Produto

class ProdutoSaida(ABC):
    @abstractmethod
    def enviar_produto(self, produto: Produto):
        pass