from fastapi import FastAPI, Body
from controller.testeController import consultarUsuarios

app = FastAPI()

@app.post("/produtos")

def cadastrarProduto(nome: str = Body(embed = True), preco: float = Body(embed = True)):
    return {
        'ação': 'Cadastrar produto', 
        'nome': nome,
        'preco': preco
    }

@app.get("/")

def inicio():
    return consultarUsuarios()

@app.post("/clientes")
    
def cadastrarClientes(nome: str = Body(embed = True), email: str = Body(embed = True), senha: str = Body(embed = True), telefone: str = Body(embed = True)):
    return {
        'ação': 'Cadastrar Cliente',
        'nome': nome,
        'emial': email,
        'senha': senha,
        'telefone': telefone
    }