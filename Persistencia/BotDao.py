from DAO import DAO
from ArquivoInvalidoException import*
from BotInexistenteException import*
from Persistencia.BotEncoder import BotEncoder
import json

class BotDAO(DAO):
    def __init__(self, datasource="bots.json"):
        super().__init__(datasource)

    def __load(self):
        bots_json = json.load(open(self.datasource, 'rb'))
        for b in bots_json['bots']:
            saudacoes = b['saudacoes']
            bot = Bot(
                b['nome'], 
                b['comandos'], 
                saudacoes['apresentacao'], 
                saudacoes['boas_vindas'], 
                saudacoes['despedida']
            )

        self.cache[bot.nome] = bot

    def __dump(self):
        json.dump(self.cache, open(self.datasource, 'wb'), cls=BotEncoder)

    def add(self, obj): #adicionar novo bot
        if isinstance(obj, Bot):
            self.cache[obj.nome] = obj  # Adiciona um objeto ao cache
            self.__dump()  # Salva o cache atualizado no arquivo
        else:
            raise ArquivoInvalidoException
        
    def get(self, key): #recuperar bot
        try:
            return self.cache[key]  # Obtém um objeto pela seu chave
        except KeyError:
            
            raise BotInexistenteException  #KeyError é "relançada" para que possa ser
        
    def remove(self, key):
        try:
            self.cache.pop(key)  # Remove um objeto pelo sua chave
            self.__dump()  # Salva o cache atualizado no arquivo
            return True
        except KeyError:
            raise BotInexistenteException # Se a chave não existe no cache, levanta uma exceção   