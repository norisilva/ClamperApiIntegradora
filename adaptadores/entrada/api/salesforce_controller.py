from flask import Blueprint, request, jsonify
from adaptadores.entrada.dto.venda_salesforce_dto import VendaSalesforceDtoSchema
from dominio.venda import Venda
from dominio.utilidade.formatar_erro import formatar_erro

salesforce_api = Blueprint("salesforce_api", __name__)
venda_salesforce_schema = VendaSalesforceDtoSchema()


@salesforce_api.route("/salesforce/novovenda", methods=["POST"])
def novo_venda():
    try:
        payload = request.get_json()
        venda_salesforce_dto = venda_salesforce_schema.load(payload)

        venda_dominio = Venda(
            codigo=venda_salesforce_dto.codigo,
            comprador=venda_salesforce_dto.comprador,
            quantidade=venda_salesforce_dto.quantidade,
            valor=venda_salesforce_dto.valor,
            codigo_produto=venda_salesforce_dto.codigo_produto,
        )

        return jsonify({
            "mensagem": "venda recebido e mapeado com sucesso.",
            "venda": {
                "codigo": venda_dominio.codigo,
                "comprador": venda_dominio.comprador,
                "quantidade": venda_dominio.quantidade,
                "valor": venda_dominio.valor,
                "codigo_produto": venda_dominio.codigo_produto
            }
        }), 201

    except Exception as e:
        response, status_code = formatar_erro(e)
        return jsonify(response), status_code