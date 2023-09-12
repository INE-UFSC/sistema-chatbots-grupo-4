from Bots.Bot import Bot

class BotFitness(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.comandos = {
            'Quero uma opinião sobre o meu treino': '\n=================\nApós uma avaliação minuciosa, percebi que você é um FRANGO !\n=================\n',
            'Treino para braço': f"\n=================\n- Comece alongando os braços\n- 3 séries de 2 minutos tentando cortar o bife do RU\n- 2 séries de 2 minutos tentando cortar a bisteca do RU\n=================\n",
            'Quero uma opinião sobre o meu shape': "\n=================\nLook at him. Nem parece que treina... Braços finos, corpo compacto e pouco aesthetic\n=================\n",
            'Adeus': "\n=================\nTudo de melhor pra você ! OUT\n=================\n"
        }

    def apresentacao(self):
        return "Eu sou o Rodrigo Goes, natural é a fonte da juventude!"
 
    def mostra_comandos(self):
        for c in range(len(self.comandos.keys())):
          print("%s - %s" % (c, self.comandos.keys()[c]))
    
    def executa_comando(self,cmd):
        print("Você disse: %s" % cmd)
        print("Rodrigo Goes: %s" % self.comandos[cmd])

    def boas_vindas(self):
        print("Qual mensagem vem aqui nas boas vindas ?")

    def despedida(self):
        print("Volte sempre meu querido Fake Natty !")