import requests
from tenacity import retry, stop_after_delay, wait_exponential, retry_if_exception_type
from dominio.excecoes.retentativa_excecao import RetentativaExcecao

class SalesforceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    @retry(
        stop=stop_after_delay(5),  # Retry for up to 5 seconds
        wait=wait_exponential(multiplier=1, min=1, max=5),  # Exponential backoff
        retry=retry_if_exception_type(requests.exceptions.RequestException)  # Retry on request exceptions
    )
    def enviar_produto(self, produto: dict) -> dict:
        try:
            url = f"{self.base_url}/salesforce/receberproduto"
            response = requests.post(url, json=produto)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RetentativaExcecao("Falha temporária ao enviar produto para o Salesforce.") from e