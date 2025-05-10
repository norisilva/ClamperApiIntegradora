from flask import Flask
from adaptadores.entrada.api.rotas import registrar_rota

def cria_api():
    app = Flask(__name__)

    registrar_rota(app)

    return app

if __name__ == "__main__":
    programa = cria_api()
    programa.run(debug=True)
