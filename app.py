#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotFitness import BotFitness

###construa a lista de bots disponíveis aqui
lista_bots = [BotFitness("Rodrigo Goes")]

sys = scb.SistemaChatBot("Fitness Bots",lista_bots)
sys.inicio()
