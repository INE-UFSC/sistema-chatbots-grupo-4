# from Persistencia.DAO import DAO
from Bots.Bot import Bot
from Persistencia.BotEncoder import BotEncoder
import json

lista_bots = []

with open('bots.json', 'r') as file_bots:
    bots_json = json.load(file_bots)

    for bot in bots_json['bots']:
        saudacoes = bot['saudacoes']
        teste = Bot(
            bot['nome'], 
            bot['comandos'], 
            saudacoes['apresentacao'], 
            saudacoes['boas_vindas'], 
            saudacoes['despedida']
        )

        lista_bots.append(teste)

for bot in lista_bots:
    # json.dump(bot)

    bot = json.dumps(bot, cls=BotEncoder)
    print(bot)
    break