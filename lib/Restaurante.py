class Restaurante():
    def __init__(self, idUsuarios, idEndenreco, nome, categoria):
        self.idUsuario = idUsuarios
        self.idEndereco = idEndenreco
        self.nome = nome
        self.categoria = categoria

###############################################################

    def getIdUsuario(self):
        return self.idUsuario

    def setIdUsuario(self, novoIdUsuario):
        self.idUsuario = novoIdUsuario
        return novoIdUsuario
    
###############################################################

    def getIdEndereco(self):
        return self.idEndereco
    
    def setIdEndereco(self, novoIdEndereco):
        self.idEndereco = novoIdEndereco
        return novoIdEndereco
    
###############################################################

    def getNome(self):
        return self.nome

    def setNome(self, novoNome):
        self.nome = novoNome
        return novoNome

###############################################################

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, novaCategoria):
        self.categoria = novaCategoria
        return novaCategoria