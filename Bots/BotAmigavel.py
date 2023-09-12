from Bots.Bot import Bot

class BotAmigavel(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.comandos = {
            1: (
                'Bom dia',
                'Bom dia, como você está? '),
            2: (
                'Conte me uma piada',
             'Por que o esqueleto não briga com ninguém? \nPorque ele não tem saco!'
            ),
            3: (
                'Quero um conselho',
                'Pegue e se cuide! Ande pela sombra sempre.'
            )
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return(f'-> Olá, sou o {self.__nome}! Fico feliz em conhecê-lo!')
 
    # def mostra_comandos(self):
    #     for i in self.__comandos:
    #         comando = self.__comandos[i]['comando']
    #         return(f'{i} - {comando}')
            
    def executa_comando(self, cmd):
        return(self.comandos[cmd][1])

    def boas_vindas(self):
        return(f'-> {self.__nome} diz: Obrigado por ter me escolhido. Espero que sejamos bons amigos.')

    def despedida(self):
        return('Pena que já acabou...')