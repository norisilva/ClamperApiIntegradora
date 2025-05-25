class RetentativaExcecao(Exception):
    def __init__(self, message="Ocorreu uma falha temporária de comunicação com um serviço interno. Tente novamente em alguns minutos."):
        super().__init__(message)