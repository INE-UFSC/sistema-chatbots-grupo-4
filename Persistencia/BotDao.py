from Persistencia.DAO import DAO
from Persistencia.ArquivoInvalidoException import*
from Persistencia.BotInexistenteException import*
from Persistencia.BotEncoder import BotEncoder
from Bots.Bot import Bot
import json

class BotDAO(DAO):
    def __init__(self, datasource="bots.json"):
        self.datasource = datasource
        self.cache = {}  # Um dicionário que atua como um cache de objetos

        try:
            self.__load()  # Tentativa de carregar os dados do arquivo

        except FileNotFoundError:
            json.dump({'bots': []}, open(self.datasource, 'w'))

    def __load(self):
        bots_json = json.load(open(self.datasource, 'r'))['bots']
        for bot in bots_json:
            saudacoes = bot['saudacoes']
            bot_obj = Bot(
                bot['nome'], 
                bot['comandos'], 
                saudacoes['apresentacao'], 
                saudacoes['boas_vindas'], 
                saudacoes['despedida']  
            )
            self.cache[bot_obj.nome] = bot_obj
        # print(self.cache)

    def __dump(self):
        encoder = BotEncoder()

        obj = { 'bots': [] }
        for bot in self.cache.values():
            bot_dict = encoder.encode(bot)
            obj['bots'].append(bot_dict)
        json.dump(obj, open(self.datasource, 'w'))

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