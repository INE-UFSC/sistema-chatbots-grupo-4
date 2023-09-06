##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {}


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos


    def mostra_comandos(self):
        self.comandos[1] = "Quero uma opinião sobre o meu treino"
        self.comandos[2] = "Treino para braço "
        self.comandos[3] = "Quero uma opinião sobre o meu shape"
        self.comandos[4] = "Adeus"
        return self.comandos
    
    @abstractmethod
    def executa_comando(self,cmd):
        pass

        
    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass

class MeuBot(Bot):
    def __init__(self, nome):
        super().__init__(nome)


    def executa_comando(self, cmd):
        if cmd == '1':
            return "\n=================\nApós uma avaliação minuciosa, percebi que você é um FRANGO !\n=================\n"
        if cmd =='2':
            return f"\n=================\n- Comece alongando os braços\n- 3 séries de 2 minutos tentando cortar o bife do RU\n- 2 séries de 2 minutos tentando cortar a bisteca do RU\n=================\n"
        if cmd =='3':
            return "\n=================\nLook at him. Nem parece que treina... Braços finos, corpo compacto e pouco aesthetic\n=================\n"
        if cmd =='4':
            return "\n=================\nTudo de melhor pra você ! OUT\n=================\n"
    
    def boas_vindas(self):
        
        print("Qual mensagem vem aqui nas boas vindas ?")
    
    def despedida(self):
        print("Volte sempre meu querido Fake Natty !")


# Criando uma instância do bot
meu_bot = MeuBot("BotFit")

##PARA TESTE DE FUNCIONAMENTO

while True:



    comandos = meu_bot.mostra_comandos()
    for chave, valor in comandos.items():
        print(f"{chave} - {valor}")

    #exibe os comandos
    controle = input("\nDigite o comando desejado (ou -1 para fechar o programa): ")
    # Configurando comandos

    if controle == '-1':
        meu_bot.despedida()
        break
    else:
        executa =  meu_bot.executa_comando(controle)
        print(executa)
