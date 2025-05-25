import requests
from tenacity import retry, stop_after_delay, wait_exponential, retry_if_exception_type
from dominio.excecoes.retentativa_excecao import RetentativaExcecao

class ClienteSalesforce:
    def __init__(self):
        self.url_base = "http://localhost:8080/api_salesforce"  # Parametrizar isto em uma configuração no futuro

    @retry(
        stop=stop_after_delay(5),  # Tentar novamente por até 5 segundos
        wait=wait_exponential(multiplier=1, min=1, max=5),  # Intervalo exponencial entre tentativas
        retry=retry_if_exception_type(requests.exceptions.RequestException)  # Tentar novamente em caso de exceções de requisição
    )
    def enviar_produto(self, produto: dict) -> dict:
        try:
            url = f"{self.url_base}/salesforce/receberproduto"
            resposta = requests.post(url, json=produto)
            resposta.raise_for_status()
            return resposta.json()
        except requests.exceptions.RequestException as e:
            raise RetentativaExcecao("Falha temporária ao enviar produto para o Salesforce.") from e