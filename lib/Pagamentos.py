class Pagamentos:
    def __init__(self, tipoPagamento, statusPagamento, valorTotal):
        self.tipoPagamento = tipoPagamento
        self.statusPagamento = statusPagamento
        self.valorTotal = valorTotal

###############################################################

    def get_tipoPagamento(self):
        return self.tipoPagamento

    def set_novoTipoPagamento(self, novoTipoPagamento):
        self.tipoPagamento = novoTipoPagamento

###############################################################

    def get_statusPagamento(self):
        return self.statusPagamento

    def set_novoStatusPagamento(self, novoStatusPagamento):
        self.statusPagamento = novoStatusPagamento

###############################################################

    def get_valorTotal(self):
        return self.valorTotal

    def set_novoValorTotal(self, novoValorTotal):
        self.valorTotal = novoValorTotal