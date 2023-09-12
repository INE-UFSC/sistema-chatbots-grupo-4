from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots:[Bot] = lista_bots
        if (any([x for x in self.__lista_bots if str(type(x)).lower()=="bot" ])):
            print("Lista de bots com objetos nao bots")
            exit()
            
        self.__bot:Bot = None
    
    def boas_vindas(self):
        print("Ola, bem vindo ao sistema fit bot!")
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('Os bots disponíveis são:')
        for i in range(len(self.__lista_bots)):
            print(i, ": ", self.__lista_bots[i].apresentacao())
        
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        while not (0 <= (bot_index := int(input())) < len(self.__lista_bots)):
            print("Bot invalido!!")
        
        self.__bot = self.__lista_bots[bot_index]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        self.mostra_comandos_bot()
        while (cmd := int(input())) > 0: 
            print(self.__bot.executa_comando(cmd))
            self.mostra_comandos_bot()

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        print(self.boas_vindas())
        
        ##mostra o menu ao usuário
        self.mostra_menu()
        
        ##escolha do bot  
        self.escolhe_bot()
        
        ##mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas())
        
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        self.le_envia_comando()
        
        ##ao sair mostrar a mensagem de despedida do bot
        print(self.__bot.despedida())