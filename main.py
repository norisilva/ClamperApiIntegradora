from flask import Flask
from infra.rotas import registrar_rota
from infra.configuracao import configuracao_por_nome
import os

def cria_api():
    app = Flask(__name__)

    nome_ambiente = os.environ.get('ENV', 'desenv')
    configuracao_atual = configuracao_por_nome.get(nome_ambiente, configuracao_por_nome['desenv'])
    app.config.from_object(configuracao_atual)

    registrar_rota(app)
    return app

if __name__ == "__main__":
    programa = cria_api()
    programa.run(debug=programa.config['MODO_DEBUG'])