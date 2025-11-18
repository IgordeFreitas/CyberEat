class Avaliacoes:
    def __init__(self, idPedido, notaServico, comentarioServico):
        self.idPedido = idPedido
        self.notaServico = notaServico
        self.comentarioServico = comentarioServico

###############################################################

    def get_idPedido(self):
        return self.idPedido

    def set_novoIdPedido(self, novoIdPedido):
        self.idPedido = novoIdPedido

###############################################################

    def get_notaServico(self):
        return self.notaServico

    def set_novoNotaServico(self, novoNotaServico):
        self.notaServico = novoNotaServico

###############################################################

    def get_comentarioServico(self):
        return self.comentarioServico

    def set_novoComentarioServico(self, novoComentarioServico):
        self.comentarioServico = novoComentarioServico