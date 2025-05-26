# API de Integração
Esta é uma API desenvolvida para integrar com o Protheus com o Sales Force, permitindo sincronização de produtos e vendas. 

**NOTICE:** Trata-se de um projeto acadêmico de livre utilização, que pode servir como base para outros projetos. Ele contempla aspectos relevantes, como recuperação de falhas produtivas, incluindo mecanismos de retry com backoff exponencial nas APIs que aciona. Entretanto, este projeto não foi projetado para uso em ambiente de produção: não possui testes unitários, nem de integração, e não segue diretrizes específicas de produção. Caso decida utilizá-lo em outros contextos, recomenda-se realizar os ajustes e adequações necessários.

## Fluxo
![Fluxo da Integração](/doc/fluxo.drawio.png)


## Como rodar a API localmente

1. Certifique-se de ter o Python 3.8+ instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/norisilva/ClamperApiIntegradora.git
   cd ClamperApiIntegradora
   
## Crie e ative um ambiente virtual:
```bash
    python -m venv venv
    source venv/bin/activate # Linux/Mac
    venv\Scripts\activate    # Windows
````

## Instale as dependências:
```pip install -r requirements.txt```

## Inicie a aplicação:
python main.py

## Como acessar a API
Após iniciar a aplicação, a API estará disponível.

## Endpoints disponíveis

POST http://127.0.0.1:5000/ClamperApiIntegradora/protheus/novoproduto

GET http://127.0.0.1:5000/ClamperApiIntegradora/

GET http://127.0.0.1:5000/ClamperApiIntegradora/health

## Informaações do projeto

RoadMap -> https://github.com/users/norisilva/projects/6/views/4
Quadro Kanban ->https://github.com/users/norisilva/projects/6/views/1
