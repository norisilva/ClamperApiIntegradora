from dataclasses import dataclass
from marshmallow import Schema, fields, post_load
from datetime import datetime

@dataclass
class VendaSalesforceDto:
    codigo: str
    comprador: str
    quantidade: int
    valor: str
    codigo_produto: int
    id_transacao: str
    timestamp: str = datetime.now().isoformat()

class VendaSalesforceDtoSchema(Schema):
    codigo = fields.Str(data_key="codigo_venda")
    comprador = fields.Str(data_key="comprador_venda")
    quantidade = fields.Str(data_key="quantidade_venda")
    valor = fields.Str(data_key="valor_venda")
    codigo_produto = fields.Int(data_key="codigo_produto_venda")
    id_transacao = fields.Str(data_key="id_transacao")
    timestamp = fields.Str(data_key="timestamp")

    @post_load
    def make_dto(self, data, **kwargs):
        return VendaSalesforceDto(**data)