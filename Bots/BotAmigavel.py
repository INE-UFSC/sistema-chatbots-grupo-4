from Bots.Bot import Bot
from Bots.Comandos import Comandos
from Bots.comandoinexistenteException import *

class BotAmigavel(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.__comandos = [Comandos(1, 'Bom dia', '\n=================\nBom dia, como você está? !\n=================\n'),
                        Comandos(2, 'Conte me uma piada', f"\n=================\n- Por que o esqueleto não briga com ninguém? \nPorque ele não tem saco!\n=================\n"),
                        Comandos(3, 'Quero um conselho', "\n=================\nPegue e se cuide! Ande pela sombra sempre.\n=================\n"),
                        Comandos(0, 'Adeus', "\n=================\nTudo de melhor pra você ! OUT\n=================\n")

        ]

    @property
    def comandos(self):
        return self.__comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return(f'Olá, sou o {self.nome}! Fico feliz em conhecê-lo!')
 

    def executa_comando(self, cmd):
        if cmd < 0 or cmd >= len(self.__comandos):
            return ComandoInexistenteExeption
        else:
            return f"Você disse: {self.comandos[cmd].mensagem}\nSobrinho do bezzos: {self.__comandos[cmd].respostas}"



    def boas_vindas(self):
        return(f'-> {self.nome} diz: Obrigado por ter me escolhido. Espero que sejamos bons amigos.')

    def despedida(self):
        return('Pena que já acabou...')