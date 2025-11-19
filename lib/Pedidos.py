class Pedidos:
    def __init__(self, idRestaurantes, idUsuarios, idEndereco, idPagamento, idEntrega):
        self._idRestaurantes = idRestaurantes
        self._idUsuarios = idUsuarios
        self._idEndereco = idEndereco
        self._idPagamento = idPagamento
        self._idEntrega = idEntrega

###############################################################

    def getIdRestaurantes(self):
        return self._idRestaurantes

    def setIdRestaurantes(self, novoIdRestaurante):
        self._idRestaurantes = novoIdRestaurante

###############################################################

    def getIdUsuarios(self):
        return self._idUsuarios

    def setIdUsuarios(self, novoIdUsuario):
        self._idUsuarios = novoIdUsuario

###############################################################

    def getIdEndereco(self):
        return self._idEndereco

    def setIdEndereco(self, novoIdEndereco):
        self._idEndereco = novoIdEndereco

###############################################################

    def getIidPagamento(self):
        return self._idPagamento

    def setIdPagamento(self, novoIdPagamento):
        self._idPagamento = novoIdPagamento

###############################################################

    def getIdEntrega(self):
        return self._idEntrega

    def setIdEntrega(self, novoIdEntrega):
        self._idEntrega = novoIdEntrega