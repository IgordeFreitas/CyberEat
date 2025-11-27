from fastapi import FastAPI, Body
import controller

app = FastAPI()

#################################################################  Abaixo, tudo sobre a rota /clientes

@app.get("/clientes")

def inicio():
    return controller.controllerUsuarios.consultarUsuarios()

@app.post("/clientes")

def cadastrarUsuario(
    nome: str = Body(embed = True),
    email: str = Body(embed = True),
    senha: str = Body(embed = True),
    telefone: str = Body(embed = True)
):
    
    return controller.controllerUsuarios.inserirUsuario(nome, email, senha, telefone)


@app.delete("/clientes")

def apagarUsuarios(idUsuario: int = Body(embed = True)):
    return controller.controllerUsuarios.deletarUsuario(idUsuario)
#################################################################  Abaixo, tudo sobre a rota /restaurantes

@app.get("/restaurante")

def restaurantes():
    return 

#################################################################  Abaixo, tudo sobre a rota /produtos


@app.post("/produtos")

def cadastrarProduto(nome: str = Body(embed = True), preco: float = Body(embed = True)):
   ...