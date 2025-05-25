from flask import Blueprint, request, jsonify
from adaptadores.entrada.dto.produto_protheus_dto import ProdutoProtheusDtoSchema
from dominio.produto import Produto
from dominio.valueobjects.fabricante import Fabricante
from dominio.valueobjects.ano import Ano
from dominio.valueobjects.nome import Nome
from dominio.utilidade.formatar_erro import formatar_erro
from fabricas.casouso import ProdutoCasoUsoFactory

protheus_api = Blueprint("protheus_api", __name__)
produto_protheus_schema = ProdutoProtheusDtoSchema()
produto_casouso = ProdutoCasoUsoFactory.criar()

@protheus_api.route("/protheus/novoproduto", methods=["POST"])
def novo_produto():
    try:
        payload = request.get_json()
        produto_protheus_dto = produto_protheus_schema.load(payload)

        produto_dominio = Produto(
            codigo=produto_protheus_dto.codigo,
            descricao=produto_protheus_dto.descricao,
            nome=Nome(produto_protheus_dto.Nome),
            fabricante=Fabricante(produto_protheus_dto.Fabricante),
            ano=Ano(produto_protheus_dto.Ano)
        )

        produto_dominio = produto_casouso.processar_produto(produto_dominio)

        return jsonify({
            "mensagem": "Produto recebido e processado com sucesso.",
            "produto": {
                "codigo": produto_dominio.codigo,
                "descricao": produto_dominio.descricao,
                "nome": produto_dominio.nome,
                "fabricante": produto_dominio.fabricante,
                "ano": produto_dominio.ano,
                "data_recepcao": produto_dominio.data_recepcao,
                "uui_recepcao": produto_dominio.uui_recepcao,
                "status_recepcao": produto_dominio.status_recepcao
            }
        }), 201

    except Exception as e:
        response, status_code = formatar_erro(e)
        return jsonify(response), status_code