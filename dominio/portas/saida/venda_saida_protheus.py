from abc import ABC, abstractmethod
from dominio.venda import Venda

class VendaSaida(ABC):
    @abstractmethod
    def enviar_venda(self, venda: Venda):
        pass