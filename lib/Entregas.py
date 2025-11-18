class Entregas:
    def __init__(self, idIndereco, dataEntrega):
        self.idIndereco = idIndereco
        self.dataEntrega = dataEntrega

###############################################################
   
    def get_idIndereco(self):
        return self.idIndereco

    def set_idIndereco(self, novoIdIndereco):
        self.idIndereco = novoIdIndereco

###############################################################

    def get_dataEntrega(self):
        return self.dataEntrega

    def set_dataEntrega(self, novaDataEntrega):
        self.dataEntrega = novaDataEntrega