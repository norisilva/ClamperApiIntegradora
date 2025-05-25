from dataclasses import dataclass
from marshmallow import Schema, fields, post_load

@dataclass
class ProdutoSalesForceDto:
    codigo: str
    descricao: str
    nome: str
    fabricante: str
    ano: int

class ProdutoProtheusDtoSchema(Schema):
    codigo = fields.Str(data_key="codigo_produto")
    descricao = fields.Str(data_key="descricao_produto")
    nome = fields.Str(data_key="nome_produto")
    fabricante = fields.Str(data_key="fabricante_produto")
    ano = fields.Int(data_key="ano_fabricacao")
    id_transacao = fields.Str(data_key="id_transacao")
    timestamp = fields.Str(data_key="timestamp")

    @post_load
    def make_dto(self, data):
        return ProdutoSalesForceDto(**data)