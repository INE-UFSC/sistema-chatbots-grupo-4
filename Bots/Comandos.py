class Comandos:
    def __init__(self, comando: int, mensagem, respostas):
        self.__comando = comando
        self.__mensagem = mensagem
        self.__respostas = respostas

    @property
    def comando(self):
        return self.__comando
    
    @comando.setter
    def comando(self, comando):
        self.__comando = comando

    @property 
    def mensagem(self):
        return self.__mensagem
    
    @mensagem.setter
    def mensagem(self, mensagem):
        self.__mensagem = mensagem

    @property
    def respostas(self):
        return self.__respostas
    
    @respostas.setter
    def respostas(self, respostas):
        self.__respostas = respostas

