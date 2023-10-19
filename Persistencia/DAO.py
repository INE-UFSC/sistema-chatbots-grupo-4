from abc import ABC, abstractmethod
import json
from Bots.Bot import*

class DAO(ABC):
    def __init__(self, datasource=''):
        self.datasource = datasource
        self.cache = {}  # Um dicionário que atua como um cache de objetos

        try:
            self.__load()  # Tentativa de carregar os dados do arquivo

        except FileNotFoundError:
            self.__dump()  # Se o arquivo não existe, cria um arquivo vazio

    def __dump(self):
        json.dump(self.cache, open(self.datasource, 'wb'))

    def __load(self):
        self.cache = json.load(open(self.datasource, 'rb'))

    def teste(self):
        return True

    @abstractmethod
    def add(self, key, obj):
        pass
    
    @abstractmethod
    def get(self, key): #recuperar bot
        pass
   
    @abstractmethod
    def remove(self, key):
        pass

    def get_all(self):
        return self.cache  # Retorna todos os objetos no cache como uma lista

