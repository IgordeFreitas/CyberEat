class Pedidos:
    def __init__(self, idRestaurantes, idUsuarios, idEndereco, idPagamento, idEntrega):
        self._idRestaurantes = idRestaurantes
        self._idUsuarios = idUsuarios
        self._idEndereco = idEndereco
        self._idPagamento = idPagamento
        self._idEntrega = idEntrega

###############################################################

    def get_idRestaurantes(self):
        return self._idRestaurantes

    def set_idRestaurantes(self, noovIdRestaurante):
        self._idRestaurantes = noovIdRestaurante

###############################################################

    def get_idUsuarios(self):
        return self._idUsuarios

    def set_idUsuarios(self, novoIdUsuario):
        self._idUsuarios = novoIdUsuario

###############################################################

    def get_idEndereco(self):
        return self._idEndereco

    def set_idEndereco(self, novoIdEndereco):
        self._idEndereco = novoIdEndereco

###############################################################

    def get_idPagamento(self):
        return self._idPagamento

    def set_idPagamento(self, novoIdPagamento):
        self._idPagamento = novoIdPagamento

###############################################################

    def get_idEntrega(self):
        return self._idEntrega

    def set_idEntrega(self, novoIdEntrega):
        self._idEntrega = novoIdEntrega