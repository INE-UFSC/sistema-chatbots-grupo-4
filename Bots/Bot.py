##implemente as seguintes classes

# from abc import ABC, abstractmethod
from Bots.Comando import Comando
import random as r

class Bot():

    def __init__(self, nome, comandos, apresentacao, boas_vindas, despedida):
        self.__nome = nome
        self.__comandos = []
        self.__saudacoes = {
            'boas_vindas': boas_vindas,
            'apresentacao': apresentacao,
            'despedida': despedida
        }

        for cmd in comandos:
            self.__comandos.append(
                Comando(cmd['pergunta'], cmd['resposta'])
                )

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

    @property
    def saudacoes(self):
        return self.__saudacoes

    @saudacoes.setter
    def saudacoes(self, saudacoes):
        self.__saudacoes = saudacoes

    def mostra_comandos(self):
        resultado = []
        for i, comando in enumerate(self.comandos):
            resultado.append(f"{i+1} - {comando.mensagem}")
        return '\n'.join(resultado)
     
    def executa_comando(self,cmd):
        if cmd < 0 or cmd-1 >= len(self.__comandos):
            return ComandoInexistenteExeption
        else:
            return f"Você disse: {self.comandos[cmd-1].mensagem}\n{self.nome}: {self.__comandos[cmd-1].respostas}"

    def apresentacao(self):
        return (self.saudacoes['apresentacao'])

    def boas_vindas(self):
        return ("%s: %s" % (self.nome, self.saudacoes['boas_vindas']))
    
    def despedida(self):
        return (self.saudacoes['despedida'])