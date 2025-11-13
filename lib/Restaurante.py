class Restaurante():
    def __init__(self, Nome, Telefone, Descriçao, Endereço, Aberto, TaxaDeEntrega, TempoMedio, CriadoEm):
        self.Nome = Nome
        self.Telfone = Telefone
        self.Descriçao = Descriçao
        self.Endereço = Endereço
        self.Aberto = Aberto
        self.TaxaDeEntrega = TaxaDeEntrega
        self.TempoMedio = TempoMedio
        self.CriadoEm = CriadoEm

###############################################################

    def setNome(self, novoNome):
        self.Nome = novoNome
        return novoNome

    def getNome(self):
        return self.Nome
    
###############################################################
    
    def setTelefone(self, novoTelefone):
        self.Telfone = novoTelefone
        return novoTelefone
    
    def getTelefone(self):
        return self.Telfone

###############################################################

    def setDescriçao(self, novaDescriaçao):
        self.Descriçao = novaDescriaçao
        return self.Descriçao
    
    def getDescriçao(self):
        return self.Descriçao
    
###############################################################
    
    def setEndereço(self, novoEndereço):
        self.Endereço = novoEndereço
        return self.Endereço
    
    def getEndereço(self):
        return self.Endereço

###############################################################

    def setAberto(self, novoAberto):
        self.Aberto = novoAberto
        return self.Aberto
    
    def getAberto(self):
        return self.Aberto
    
###############################################################

    def setTaxaDeEentrega(self, novaTaxaDeEntrega):
        self.TaxaDeEntrega = novaTaxaDeEntrega
        return self.TaxaDeEntrega
    
    def getTaxaDeEntrega(self):
        return self.TaxaDeEntrega
    
###############################################################

    def setTempoMedio(self, novoTempoMedio):
        self.TempoMedio = novoTempoMedio
        return self.TempoMedio
    
    def getTempoMedio(self):
        return self.TempoMedio
    
###############################################################

    def setCriadoEm(self, novaCriadoEm):
        self.CriadoEm = novaCriadoEm
        return self.CriadoEm
    
    def getCriadoEm(self):
        return self.CriadoEm
    
###############################################################
