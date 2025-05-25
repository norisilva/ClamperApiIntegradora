from infra.cliente.salesforce_client import ClienteSalesforce
from adaptadores.saida.api.salesforce_adapter import SalesforceAdapter
from dominio.casosdeuso.produto_casouso import ProdutoCasoUso

class ProdutoCasoUsoFactory:
    @staticmethod
    def criar() -> ProdutoCasoUso:
        salesforce_client = ClienteSalesforce()
        salesforce_adapter = SalesforceAdapter(salesforce_client)
        return ProdutoCasoUso(salesforce_adapter)