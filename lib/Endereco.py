class Endereco():
    def __init__(self, id_usuario, bairro):
        self.id_usuario = id_usuario
        self.bairro = bairro

    ###############################################################

    def setIdUsuario(self, novoIdUsuario):
        self.id_usuario = novoIdUsuario
        return novoIdUsuario

    def getIdUsuario(self):
        return self.id_usuario

    ###############################################################

    def setBairro(self, novoBairro):
        self.bairro = novoBairro
        return novoBairro

    def getBairro(self):
        return self.bairro