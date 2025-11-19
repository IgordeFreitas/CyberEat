class Avaliacoes:
    def __init__(self, idPedido, notaServico, comentarioServico):
        self.idPedido = idPedido
        self.notaServico = notaServico
        self.comentarioServico = comentarioServico

###############################################################

    def getIdPedido(self):
        return self.idPedido

    def setNovoIdPedido(self, novoIdPedido):
        self.idPedido = novoIdPedido

###############################################################

    def getNotaServico(self):
        return self.notaServico

    def setNovoNotaServico(self, novoNotaServico):
        self.notaServico = novoNotaServico

###############################################################

    def getComentarioServico(self):
        return self.comentarioServico

    def setNovoComentarioServico(self, novoComentarioServico):
        self.comentarioServico = novoComentarioServico