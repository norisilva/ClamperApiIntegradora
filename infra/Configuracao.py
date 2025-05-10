import os

class ConfiguracaoBase:
    MODO_DEBUG = False
    MODO_TESTE = False
    CHAVE_SECRETA = os.environ.get("CHAVE_SECRETA", "minha-chave-padrao")
    JSON_ORDENAR_CHAVES = False
    JSON_AS_ASCII = False  # Moved here

class ConfiguracaoDesenvolvimento(ConfiguracaoBase):
    MODO_DEBUG = True

class ConfiguracaoProducao(ConfiguracaoBase):
    pass

class ConfiguracaoTeste(ConfiguracaoBase):
    MODO_TESTE = True
    MODO_DEBUG = True

configuracao_por_nome = {
    "desenv": ConfiguracaoDesenvolvimento,
    "prod": ConfiguracaoProducao,
    "teste": ConfiguracaoTeste
}