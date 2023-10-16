class BotInexistenteException(KeyError):
    def __init__(self, *args: object) -> None:
        super().__init__("Bot não encontrado")