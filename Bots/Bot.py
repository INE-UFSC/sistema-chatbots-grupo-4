##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {}

    #nao esquecer o decorator

    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self,comandos):
        self.comandos = self.__comandos

    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass