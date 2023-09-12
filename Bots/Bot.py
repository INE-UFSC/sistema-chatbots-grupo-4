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
        for c in self.comandos.keys():
            print("%s - %s" % (c, self.comandos[c][0]))
    
    @abstractmethod
    def executa_comando(self,cmd):
        pass
        
    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass