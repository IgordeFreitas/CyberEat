class Endereco():
    def __init__(self, apelido, rua, numero, complimento, pontoReferencia, bairro, cidade):
        self.apelido = apelido
        self.rua = rua
        self.numero = numero
        self.complimento = complimento
        self.p_referencia = pontoReferencia
        self.bairro = bairro
        self.cidade = cidade

###############################################################

    def setApelido(self, novoApelido):
        self.apelido = novoApelido
        return novoApelido

    def getApelido(self):
        return self.apelido
    
###############################################################
    
    def setRua(self, novaRua):
        self.rua = novaRua
        return novaRua
    
    def getRua(self):
        return self.rua

###############################################################

    def setNumero(self, novoNumero):
        self.numero = novoNumero
        return self.numero
    
    def getNumero(self):
        return self.numero
    
###############################################################
    
    def setComplimento(self, novocomlimento):
        self.complimento = novocomlimento
        return self.complimento
    
    def getComplimento(self):
        return self.complimento

###############################################################

    def setBairro(self, novoBairro):
        self.bairro = novoBairro
        return self.bairro
    
    def getBairro(self):
        return self.bairro
    
###############################################################

    def setPontoReferencia(self, novoPontoReferencia):
        self.p_referencia = novoPontoReferencia
        return self.p_referencia
    
    def getPontoReferencia(self):
        return self.p_referencia
    
###############################################################

    def setCidade(self, novaCidade):
        self.cidade = novaCidade
        return self.cidade
    
    def getCidade(self):
        return self.cidade