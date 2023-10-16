class ArquivoInvalidoException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Arquivo inválido para adicionar novo bot")