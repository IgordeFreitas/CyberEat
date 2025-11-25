class ItensPedido:
    def __init__(self, idPedido, nomeItem, quantidadeItem, precoUnitario):
        self.idPedido = idPedido
        self.nomeItem = nomeItem
        self.uantidadeItem = quantidadeItem
        self.precoUnitario = precoUnitario

###############################################################

    def getIdPedido(self):
        return self.idPedido

    def setNovoIdPedido(self, novoIdPedido):
        self.idPedido = novoIdPedido

###############################################################

    def getNomeItem(self):
        return self.nomeItem

    def setNovoNomeItem(self, novoNomeItem):
        self.nomeItem = novoNomeItem

###############################################################

    def getQuantidadeItem(self):
        return self.uantidadeItem

    def setNovoQuantidadeItem(self, novoQuantidadeItem):
        self.uantidadeItem = novoQuantidadeItem

###############################################################

    def getPrecoUnitario(self):
        return self.precoUnitario

    def setNovoPrecoUnitario(self, novoPrecoUnitario):
        self.precoUnitario = novoPrecoUnitario