class Usuarios():
    def __init__(self, nome, CPF, emial, senha, telefone):
        self.nome = nome
        self.cpf = CPF
        self.email = emial
        self.senha = senha
        self.telefone = telefone

######################################################

    def setNome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def getNOme(self):
        return self.nome
    
####################################################### 
    
    def setCPF(self, novo_CPF):
        self.cpf = novo_CPF
        return self.cpf
        
    def getCPF(self):
        return self.cpf
    
#######################################################

    def setEmail(self, novo_emial):
        self.email = novo_emial
        return self.email

    def getEmail(self):
        return self.email
    
#######################################################    

    def setSenha(self, nova_senha):
        self.senha = nova_senha
        return self.senha
        
    def getSenha(self):
        return self.senha
    
#######################################################

    def setTelefone(self, novo_telefone):
        self.telefone = novo_telefone
        return self.telefone

    def getTelefone(self):
        return self.telefone
