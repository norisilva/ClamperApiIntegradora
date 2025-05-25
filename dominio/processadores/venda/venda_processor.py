import uuid
from datetime import datetime
from dominio.venda import Venda
from dominio.portas.saida.venda_saida_protheus import VendaSaida
from dominio.excecoes.retentativa_excecao import RetentativaExcecao

RECEBIDO_COM_SUCESSO = "Recebido com sucesso"

class VendaProcessor:
    def __init__(self, venda_saida: VendaSaida):
        self.venda_saida = venda_saida

    def processar_venda(self, venda: Venda) -> Venda:
        print("Processando venda: %s", venda.codigo)

        venda.data_recepcao = datetime.now()
        venda.uui_recepcao = str(uuid.uuid4())
        venda.status_recepcao = RECEBIDO_COM_SUCESSO

        print("Venda processada com sucesso: %s", venda.codigo)

        try:
            self.venda_saida.enviar_venda(venda)
        except RetentativaExcecao as e:
            raise RetentativaExcecao(f"Erro temporário ao enviar venda: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Erro ao processar venda: {str(e)}")

        return venda