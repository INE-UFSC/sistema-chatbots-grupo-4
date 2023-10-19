from Bots.Bot import Bot
from json import JSONEncoder

class BotEncoder():
  def encode(self, bot_raw: Bot):
    bot_dict = {
      'nome': bot_raw.nome,
      'saudacoes': {
        'boas_vindas': bot_raw.saudacoes['boas_vindas'],
        'apresentacao': bot_raw.saudacoes['apresentacao'],
        'despedida': bot_raw.saudacoes['despedida']
      },
      'comandos': [
        { 'pergunta': i.mensagem, 'resposta': i.respostas } for i in bot_raw.comandos
      ]
    }

    return bot_dict