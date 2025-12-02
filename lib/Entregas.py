class Entregas:
    def __init__(self, idEndereco, dataEntrega):
        self.idEndereco = idEndereco
        self.dataEntrega = dataEntrega

###############################################################
   
    def getIdEndereco(self):
        return self.idEndereco

    def setIdEndereco(self, novoIdEndereco):
        self.idEndereco = novoIdEndereco

###############################################################

    def getDataEntrega(self):
        return self.dataEntrega

    def setDataEntrega(self, novaDataEntrega):
        self.dataEntrega = novaDataEntrega