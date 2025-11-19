class Pagamentos:
    def __init__(self, tipoPagamento, statusPagamento, valorTotal):
        self.tipoPagamento = tipoPagamento
        self.statusPagamento = statusPagamento
        self.valorTotal = valorTotal

###############################################################

    def getTipoPagamento(self):
        return self.tipoPagamento

    def setNovoTipoPagamento(self, novoTipoPagamento):
        self.tipoPagamento = novoTipoPagamento

###############################################################

    def getStatusPagamento(self):
        return self.statusPagamento

    def setNovoStatusPagamento(self, novoStatusPagamento):
        self.statusPagamento = novoStatusPagamento

###############################################################

    def getValorTotal(self):
        return self.valorTotal

    def setNovoValorTotal(self, novoValorTotal):
        self.valorTotal = novoValorTotal