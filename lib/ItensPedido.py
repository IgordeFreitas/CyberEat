class ItensPedido:
    def __init__(self, idPedido, nomeItem, quantidadeItem, precoUnitario):
        self.idPedido = idPedido
        self.nomeItem = nomeItem
        self.uantidadeItem = quantidadeItem
        self._precoUnitario = precoUnitario

###############################################################

    def get_idPedido(self):
        return self.idPedido

    def set_novoIdPedido(self, novoIdPedido):
        self.idPedido = novoIdPedido

###############################################################

    def get_nomeItem(self):
        return self.nomeItem

    def set_novoNomeItem(self, novoNomeItem):
        self.nomeItem = novoNomeItem

###############################################################

    def get_quantidadeItem(self):
        return self.uantidadeItem

    def set_novoQuantidadeItem(self, novoQuantidadeItem):
        self.uantidadeItem = novoQuantidadeItem

###############################################################

    def get_precoUnitario(self):
        return self._precoUnitario

    def set_novoPrecoUnitario(self, novoPrecoUnitario):
        self._precoUnitario = novoPrecoUnitario