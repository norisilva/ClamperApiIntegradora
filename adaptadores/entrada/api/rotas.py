from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "disponível"})

@api.route("/", methods=["GET"])
def home():
    return "Bem-vindo à API Integradora da empresa Clamper. A API recebe e envia dados disparados por scripts do sistema Protheus e do Sales Force, automaticamente, não sendo necessário ação do ser humano."

def registrar_rota(app):
    app.register_blueprint(api, url_prefix="/ClamperApiIntegradora")
