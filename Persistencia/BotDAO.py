from Persistencia.DAO import DAO
from Bots.Bot import Bot

class BotDAO(DAO):
    def __init__(self):
        super().__init__('Bot.pkl')

    
    def add(self, bot: Bot):
        if (bot is not None) and isinstance(bot, Bot):
            super().add(bot.nome, bot.comandos)

    def get(self