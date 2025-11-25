class Pedidos:
    def __init__(self, idRestaurantes, idUsuarios, idEndereco, idPagamento, idEntrega):
        self.idRestaurantes = idRestaurantes
        self.idUsuarios = idUsuarios
        self.idEndereco = idEndereco
        self.idPagamento = idPagamento
        self.idEntrega = idEntrega

###############################################################

    def getIdRestaurantes(self):
        return self.idRestaurantes

    def setIdRestaurantes(self, novoIdRestaurante):
        self.idRestaurantes = novoIdRestaurante

###############################################################

    def getIdUsuarios(self):
        return self.idUsuarios

    def setIdUsuarios(self, novoIdUsuario):
        self.idUsuarios = novoIdUsuario

###############################################################

    def getIdEndereco(self):
        return self.idEndereco

    def setIdEndereco(self, novoIdEndereco):
        self.idEndereco = novoIdEndereco

###############################################################

    def getIidPagamento(self):
        return self.idPagamento

    def setIdPagamento(self, novoIdPagamento):
        self.idPagamento = novoIdPagamento

###############################################################

    def getIdEntrega(self):
        return self.idEntrega

    def setIdEntrega(self, novoIdEntrega):
        self.idEntrega = novoIdEntrega