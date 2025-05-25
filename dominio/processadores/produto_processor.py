import uuid
from datetime import datetime
from dominio.produto import Produto
from adaptadores.saida.api.salesforce_adapter import SalesforceAdapter
from dominio.excecoes.retentativa_excecao import RetentativaExcecao

RECEBIDO_COM_SUCESSO = "Recebido com sucesso"


class ProdutoProcessor:
    def __init__(self, salesforce_adapter: SalesforceAdapter):
        self.salesforce_adapter = salesforce_adapter

    def processar_produto(self, produto: Produto) -> Produto:
        print("Processando produto: %s", produto.codigo)

        produto.data_recepcao = datetime.now()
        produto.uui_recepcao = str(uuid.uuid4())
        produto.status_recepcao = RECEBIDO_COM_SUCESSO

        print("Produto processado com sucesso: %s", produto.codigo)

        try:
            self.salesforce_adapter.enviar_produto(produto)
        except RetentativaExcecao as e:
            raise RetentativaExcecao(f"Erro temporário ao enviar produto: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Erro ao processar produto: {str(e)}")

        return produto