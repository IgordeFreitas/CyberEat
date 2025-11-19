class Entregas:
    def __init__(self, idIndereco, dataEntrega):
        self.idIndereco = idIndereco
        self.dataEntrega = dataEntrega

###############################################################
   
    def getIdIndereco(self):
        return self.idIndereco

    def setIdIndereco(self, novoIdIndereco):
        self.idIndereco = novoIdIndereco

###############################################################

    def getDataEntrega(self):
        return self.dataEntrega

    def setDataEntrega(self, novaDataEntrega):
        self.dataEntrega = novaDataEntrega