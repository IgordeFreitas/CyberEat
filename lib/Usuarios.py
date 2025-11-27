class Usuarios():
    def __init__(self, nome, email, senha, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone

######################################################

    def setNome(self, novoNome):
        self.nome = novoNome
        return self.nome

    def getNome(self):
        return self.nome
    
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
