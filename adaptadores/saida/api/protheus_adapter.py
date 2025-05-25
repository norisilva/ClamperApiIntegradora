from infra.cliente.protheus_client import ClienteProtheus
from dominio.produto import Produto
from dominio.portas.saida.produto_saida_salesforce import ProdutoSaida

class ProtheusAdapter(ProdutoSaida):
    def __init__(self, client: ClienteProtheus):
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
        return self.client.enviar_venda(produto_dict)
