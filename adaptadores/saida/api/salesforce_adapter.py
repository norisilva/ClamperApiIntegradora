from infra.client.salesforce_client import SalesforceClient
from dominio.produto import Produto

class SalesforceAdapter:
    def __init__(self, client: SalesforceClient):
        self.client = client

    def enviar_produto(self, produto: Produto) -> dict:
        produto_dict = {
            "codigo": produto.codigo,
            "descricao": produto.descricao,
            "nome": produto.nome,
            "fabricante": produto.fabricante,
            "ano": produto.ano,
            "data_recepcao": produto.data_recepcao.isoformat(),
            "uui_recepcao": produto.uui_recepcao,
            "status_recepcao": produto.status_recepcao
        }
        return self.client.enviar_produto(produto_dict)