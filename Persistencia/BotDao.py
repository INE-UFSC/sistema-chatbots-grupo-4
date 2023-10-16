from DAO import DAO
from ArquivoInvalidoException import*
from BotInexistenteException import*


class BotDAO(DAO):
    def __init__(self, datasource="bots.json"):
        super().__init__(datasource)



    def add(self, key, obj): #adicionar novo bot
        if isinstance(key, Bot):
            self.cache[key] = obj  # Adiciona um objeto ao cache
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