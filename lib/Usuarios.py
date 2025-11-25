class Usuarios():
    def __init__(self, nome, CPF, emial, senha, telefone):
        self.nome = nome
        self.cpf = CPF
        self.email = emial
        self.senha = senha
        self.telefone = telefone

######################################################

    def setNome(self, novoNome):
        self.nome = novoNome
        return self.nome

    def getNOme(self):
        return self.nome
    
####################################################### 
    
    def setCPF(self, novoCPF):
        self.cpf = novoCPF
        return self.cpf
        
    def getCPF(self):
        return self.cpf
    
#######################################################

    def setEmail(self, novoEmial):
        self.email = novoEmial
        return self.email

    def getEmail(self):
        return self.email
    
#######################################################    

    def setSenha(self, novaSenha):
        self.senha = novaSenha
        return self.senha
        
    def getSenha(self):
        return self.senha
    
#######################################################

    def setTelefone(self, novoTelefone):
        self.telefone = novoTelefone
        return self.telefone

    def getTelefone(self):
        return self.telefone
