from fastapi import FastAPI, Body
from controller.testeController import *

app = FastAPI()

#################################################################  Abaixo, tudo sobre a rota /clientes

@app.get("/clientes")

def inicio():
    return consultarUsuarios()

@app.post("/clientes")

def cadastrarUsuario(
    nome: str = Body(embed = True),
    email: str = Body(embed = True),
    senha: str = Body(embed = True),
    telefone: str = Body(embed = True)
):
    
    return inserirUsuario(nome, email, senha, telefone)


@app.delete("/clientes")

def apagarUsuarios(idUsuario: int = Body(embed = True)):
    return deletarUsuario(idUsuario)
#################################################################  Abaixo, tudo sobre a rota /restaurantes

@app.get("/restaurante")

def restaurantes():
    return 

#################################################################  Abaixo, tudo sobre a rota /produtos


@app.post("/produtos")

def cadastrarProduto(nome: str = Body(embed = True), preco: float = Body(embed = True)):
    return {
        'nome': nome,
        'preco': preco
    }