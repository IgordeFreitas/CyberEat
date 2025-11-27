from fastapi import FastAPI, Body
from controller import controllerUsuarios, controllerRestaurante, controllerAvaliacoes, controllerEndereco, controllerEntregas, controllerItensPedidos, controllerPagamentos, controllerPedidos

app = FastAPI()

#################################################################  Abaixo, tudo sobre a rota /clientes

@app.get("/clientes")

def consultUsuarios():
    return controllerUsuarios.consultarUsuarios()

@app.post("/clientes")

def cadastrarUsuario(
    nome: str = Body(embed = True),
    email: str = Body(embed = True),
    senha: str = Body(embed = True),
    telefone: str = Body(embed = True)
):
   
    return controllerUsuarios.inserirUsuario(nome, email, senha, telefone)

@app.delete("/clientes")

def apagarUsuarios(idUsuario: int = Body(embed = True)):
    return controllerUsuarios.deletarUsuario(idUsuario)


#################################################################  Abaixo, tudo sobre a rota /restaurantes

@app.get("/restaurantes")

def restaurantes():
    return controllerRestaurante.consultarRestaurantes()

@app.post("/restaurantes")

def cadastrarRestaurante(
    id_usuario: int = Body(embed = True),
    id_endereco: int = Body(embed = True),
    nome_restaurante: str = Body(embed = True),
    categoria: str = Body(embed = True),
):
    return controllerRestaurante.inserirRestaurantes(id_usuario, id_endereco, nome_restaurante, categoria)

@app.delete("/restaurantes")

def deletarRestaurantes(id_restaurantes: int = Body(embed = True)):
    return controllerRestaurante.deletarRestaurante(id_restaurantes)
    
#################################################################  Abaixo, tudo sobre a rota /pedidos


@app.get("/pedidos")

def consultPedidos():
    return controllerPedidos.consultarPedidos()


@app.post("/pedidos")

def cadastrarPedidos(
    id_restaurantes: int = Body(embed = True),
    id_usuarios: int = Body(embed = True),
    id_Endereco: int = Body(embed = True),
    id_Pagamento: int = Body(embed = True),
    id_Entrega: int = Body(embed = True),
):
    return controllerPedidos.inserirPedidos(id_restaurantes, id_usuarios, id_Endereco, id_Pagamento, id_Entrega)