from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from adaptadores.entrada.dto.produto_protheus_dto import ProdutoProtheusDtoSchema
from dominio.entidades.produto import Produto
from dominio.entidades.types.fabricante import fabricante
from dominio.entidades.types.nome import nome
from dominio.entidades.types.ano import ano

protheus_api = Blueprint("protheus_api", __name__)
produto_protheus_schema = ProdutoProtheusDtoSchema()


@protheus_api.route("/protheus/novoproduto", methods=["POST"])
def novo_produto():
    try:

        payload = request.get_json()
        produto_protheus_dto = produto_protheus_schema.load(payload)

        produto_dominio = Produto(
            codigo=produto_protheus_dto.codigo,
            descricao=produto_protheus_dto.descricao,
            nome=nome(produto_protheus_dto.nome),
            fabricante=fabricante(produto_protheus_dto.fabricante),
            ano=ano(produto_protheus_dto.ano)
        )

        return jsonify({
            "mensagem": "Produto recebido e mapeado com sucesso.",
            "produto": {
                "codigo": produto_dominio.codigo,
                "descricao": produto_dominio.descricao,
                "nome": produto_dominio.nome,
                "fabricante": produto_dominio.fabricante,
                "ano": produto_dominio.ano
            }
        }), 201

    except ValidationError as e:
        return jsonify({"erro": "Erro de validação", "details": e.messages}), 400
    except Exception as e:
        return jsonify({"erro": "Erro interno do servidor", "details": str(e)}), 500