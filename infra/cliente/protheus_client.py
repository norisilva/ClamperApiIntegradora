import requests
from tenacity import retry, stop_after_delay, wait_exponential, retry_if_exception_type
from dominio.excecoes.retentativa_excecao import RetentativaExcecao

class ClienteProtheus:
    def __init__(self):
        self.url_base = "http://localhost:8080/api_protheus"  # Parametrizar no futuro

    @retry(
        stop=stop_after_delay(5),  # Tenta por até 5 segundos
        wait=wait_exponential(multiplier=1, min=1, max=5),
        retry=retry_if_exception_type(requests.exceptions.RequestException)
    )
    def enviar_venda(self, venda: dict) -> dict:
        try:
            url = f"{self.url_base}/protheus/recebervenda"
            resposta = requests.post(url, json=venda)
            resposta.raise_for_status()
            return resposta.json()
        except requests.exceptions.RequestException as e:
            raise RetentativaExcecao("Falha temporária ao enviar venda para o Protheus.") from e
