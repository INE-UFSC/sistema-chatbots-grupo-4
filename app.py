#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
# from Bots.BotFitness import BotFitness
# from Bots.BotAmigavel import BotAmigavel

# from Persistencia.DAO import DAO
from Bots.Bot import Bot
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

# for bot in lista_bots:
#     print(bot.comandos)

###construa a lista de bots disponíveis aqui
# lista_bots = [BotFitness("Rodrigo Goes"), BotAmigavel("Bot sobrinho do bezos")]

sys = scb.SistemaChatBot("Fitness Bots",lista_bots)
sys.inicio()
