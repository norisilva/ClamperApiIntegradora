from dominio.produto import Produto
from dominio.processadores.produto.produto_processor import ProdutoProcessor
from dominio.portas.saida.produto_saida_salesforce import ProdutoSaida

class ProdutoCasoUso:
    def __init__(self, produto_saida: ProdutoSaida):
        self.produto_processor = ProdutoProcessor(produto_saida)

    def processar_produto(self, produto: Produto) -> Produto:
        return self.produto_processor.processar_produto(produto)