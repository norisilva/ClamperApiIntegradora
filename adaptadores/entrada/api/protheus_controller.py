from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from adaptadores.entrada.dto.produto_protheus_dto import ProdutoProtheusDtoSchema
from dominio.produto import Produto
from dominio.valueobjects.fabricante import Fabricante
from dominio.valueobjects import nome
from dominio.valueobjects.ano import Ano
from dominio.utilidade.formatar_erro import formatar_erro

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
            nome=nome(produto_protheus_dto.Nome),
            fabricante=Fabricante(produto_protheus_dto.Fabricante),
            ano=Ano(produto_protheus_dto.Ano)
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

    except Exception as e:
        response, status_code = formatar_erro(e)
        return jsonify(response), status_code