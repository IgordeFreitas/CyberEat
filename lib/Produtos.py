class Produtos:
    def __init__(self, idRestaurante, descricao):
        self.idRestaurante = idRestaurante
        self.descricao = descricao

######################################################

    def getIdRestaurante(self):
        return self.idRestaurante

    def setIdRestaurante(self, novoIdRestaurante):
        self.idRestaurante = novoIdRestaurante

######################################################

    def getDescricaoProduto(self):
        return self.descricao

    def setDescricaoProduto(self, novaDescricao):
        self.descricao = novaDescricao

