from abc import ABC
import pickle

class DAO(ABC):
    def __init__(self, datasource=''):
        self.datasource = datasource
        self.cache = {}  # Um dicionário que atua como um cache de objetos

        try:
            self.__load()  # Tentativa de carregar os dados do arquivo

        except FileNotFoundError:
            self.__dump()  # Se o arquivo não existe, cria um arquivo vazio

    def __dump(self):
        pickle.dump(self.cache, open(self.datasource, 'wb'))

    def __load(self):
        self.cache = pickle.load(open(self.datasource, 'rb'))

    def add(self, key, obj):
        self.cache[key] = obj  # Adiciona um objeto ao cache
        self.__dump()  # Salva o cache atualizado no arquivo

    def get(self, key):
        try:
            return self.cache[key]  # Obtém um objeto pela seu chave
        except KeyError:
            print('Chave não encontrada', f = sys.stderr)  # Se a chave não existe no cache, retorna None
            raise KeyError #KeyError é "relançada" para que possa ser tratada em um nível superior do código.
   
    def remove(self, key):
        try:
            self.cache.pop(key)  # Remove um objeto pelo sua chave
            self.__dump()  # Salva o cache atualizado no arquivo
            return True
        except KeyError:
            raise  # Se a chave não existe no cache, levanta uma exceção

    def get_all(self):
        return list(self.cache.values())  # Retorna todos os objetos no cache como uma lista
