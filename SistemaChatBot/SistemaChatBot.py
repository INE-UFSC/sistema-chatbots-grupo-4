from Bots.Bot import Bot
from Persistencia.BotDao import BotDAO
from Persistencia.DAO import DAO
from interface.Interface import Interface

class SistemaChatBot:
    def __init__(self,nomeEmpresa):
        self.__empresa=nomeEmpresa
        self.dao = BotDAO()
        
        self.__lista_bots = self.dao.get_all()
        if (any([x for x in self.__lista_bots.values() if str(type(x)).lower()=="bot" ])):
            print("Lista de bots com objetos nao bots")
            exit()
            
        self.__bot:Bot = None
        
    @property
    def lista_bots(self):
        return self.__lista_bots
        
    def salvar(self, bot):
        self.dao.add(bot)

    def inicio(self):
        Interface(self)
