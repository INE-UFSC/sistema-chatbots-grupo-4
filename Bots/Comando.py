class Comando:
    def __init__(self, mensagem, respostas):
        self.__mensagem = mensagem
        self.__respostas = respostas

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

