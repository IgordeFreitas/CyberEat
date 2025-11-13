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