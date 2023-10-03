from Bots.Bot import Bot
from Bots.Comandos import Comandos

class BotFitness(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [Comandos(1, 'Quero uma opinião sobre o meu treino', '\n=================\nApós uma avaliação minuciosa, percebi que você é um FRANGO !\n=================\n'),
                            Comandos(2, 'Treino para braço', f"\n=================\n- Comece alongando os braços\n- 3 séries de 2 minutos tentando cortar o bife do RU\n- 2 séries de 2 minutos tentando cortar a bisteca do RU\n=================\n"),
                            Comandos(3, 'Quero uma opinião sobre o meu shape', "\n=================\nLook at him. Nem parece que treina... Braços finos, corpo compacto e pouco aesthetic\n=================\n"),
                            Comandos(0, 'Adeus', "\n=================\nTudo de melhor pra você ! OUT\n=================\n")
                           
                           ] #cada comando é um objeto da classe comando
        


    def apresentacao(self):
        return "Eu sou o Rodrigo Goes, natural é a fonte da juventude!"

    def executa_comando(self,cmd):
    
    if self.comandos[cmd].resposta == None:
        pass #fazer o tratamento de erro
    else:
        return  ("Você disse: %s" % self.comandos[cmd][0]) + ("\nRodrigo Goes: %s" % self.comandos[cmd][1])
    
    def boas_vindas(self):
        return ("Obrigado por me escolher!")

    def despedida(self):
        return ("Volte sempre meu querido Fake Natty !")
