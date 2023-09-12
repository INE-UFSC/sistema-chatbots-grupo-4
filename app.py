#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotFitness import BotFitness
from Bots.BotAmigavel import BotAmigavel

###construa a lista de bots disponíveis aqui
lista_bots = [BotFitness("Rodrigo Goes"), BotAmigavel("Bot sobrinho do bezos")]

sys = scb.SistemaChatBot("Fitness Bots",lista_bots)
sys.inicio()
