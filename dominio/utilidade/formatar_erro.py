def formatar_erro(exception):
    """Formats the error response based on the exception attributes."""
    response = {
        "erro": getattr(exception, "message", "Erro interno do servidor"),
        "detalhes": getattr(exception, "detalhes", str(exception)),
        "instrucoes": getattr(exception, "instrucoes", "Consulte o administrador do sistema.")
    }
    status_code = getattr(exception, "status_code", 500)
    return response, status_code