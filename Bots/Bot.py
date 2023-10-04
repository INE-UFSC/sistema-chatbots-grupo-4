##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = []


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
        resultado = []
        for i, comando in enumerate(self.comandos):
            resultado.append(f"{i} - {comando.mensagem}")
        return '\n'.join(resultado)
     
    
    @abstractmethod
    def executa_comando(self,cmd):
        pass
        
    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass