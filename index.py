from fastapi import FastAPI, Body
from controller import controllerUsuarios, controllerRestaurante, controllerAvaliacoes, controllerEndereco, controllerEntregas, controllerItensPedidos, controllerPagamentos, controllerPedidos, controllerProdutos
app = FastAPI()

#################################################################  Abaixo, tudo sobre a rota /clientes

@app.get("/usuarios")

def consultUsuarios():
    return controllerUsuarios.consultarUsuarios()

@app.post("/usuarios")

def cadastrarUsuario(
    nome: str = Body(embed = True),
    email: str = Body(embed = True),
    senha: str = Body(embed = True),
    telefone: str = Body(embed = True)
):
   
    return controllerUsuarios.inserirUsuario(nome, email, senha, telefone)

@app.delete("/usuarios")

def apagarUsuarios(idUsuario: int = Body(embed = True)):
    return controllerUsuarios.deletarUsuario(idUsuario)

@app.patch("/usuarios")

def alterarUsuario(
    nome: str = Body(embed = True),
    email: str = Body(embed = True),
    senha: str = Body(embed = True),
    telefone: str = Body(embed = True),
    idUsuario: int = Body(embed = True)
):
    return controllerUsuarios.atualizarUsuario(nome, email, senha, telefone, idUsuario)

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

@app.patch("/restaurantes")

def alterarRestaurante(
       idUsuario: int = Body(embed = True),
       idEndereco: int = Body(embed = True),
       nomeRestaurante: str = Body(embed = True),
       categoria: str = Body(embed = True),
       idRestaurante: int = Body(embed = True)
):
    return controllerRestaurante.alterarRestaurante(idUsuario, idEndereco, nomeRestaurante, categoria, idRestaurante)
    
#################################################################  Abaixo, tudo sobre a rota /pedidos


@app.get("/pedidos")

def consultPedidos():
    return controllerPedidos.consultarPedidos()


@app.post("/pedidos")

def cadastrarPedidos(
    id_restaurantes: int = Body(embed = True),
    id_usuarios: int = Body(embed = True),
    id_Endereco: int = Body(embed = True),
    id_pagamento: int = Body(embed = True),
    id_Entrega: int = Body(embed = True),
):
    return controllerPedidos.inserirPedidos(id_restaurantes, id_usuarios, id_Endereco, id_pagamento, id_Entrega)

@app.delete("/pedidos")

def deletarPedidos(id_pedido: int = Body(embed = True)):
    controllerPedidos.deletarPedidos(id_pedido)


@app.patch('/pedidos')

def alterarPedido(
    id_restaurante: int = Body(embed = True), 
    id_usuarios: int = Body(embed = True), 
    id_endereco: int = Body(embed = True), 
    id_pagamento: int = Body(embed = True), 
    id_entrega: int = Body(embed = True), 
    idPedido: int = Body(embed = True)
):
    return controllerPedidos.alterarPedidos(id_restaurante, id_usuarios, id_endereco, id_pagamento, id_entrega, idPedido)


#################################################################  Abaixo, tudo sobre a rota /entregas

@app.get("/entregas")

def consultEntregas():
    return controllerEntregas.consultarEntregas()

@app.post("/entregas")

def cadastrarEntrega(
    id_endereco: int = Body(embed = True),
    data_entrega: str = Body(embed = True)
):
   
    return controllerEntregas.inserirEntregas(id_endereco, data_entrega)

@app.delete("/entregas")

def apagarUsuarios(id_entrega: int = Body(embed = True)):
    return controllerEntregas.deletarEntregas(id_entrega)


#################################################################  Abaixo, tudo sobre a rota /produtos

@app.get("/produtos")

def consultProdutos():
    return controllerProdutos.consultarProdutos()

@app.post("/produtos")

def cadastrarProdutos(
    id_restaurantes: int = Body(embed = True),
    descricao: str = Body(embed = True)
):
   
    return controllerProdutos.inserirProdutos(id_restaurantes, descricao)

@app.delete("/produtos")

def apagarProdutos(id_produto: int = Body(embed = True)):
    return controllerProdutos.deletarProdutos(id_produto)


@app.patch("/produtos")

def alterarProdutos(
    idRestaurante: int = Body(embed = True),
    descricao: str = Body(embed = True),
    idProduto: int = Body(embed = True)
):
    return controllerProdutos.alterarProdutos(idRestaurante, descricao, idProduto)


########################################################

@app.get("/pagamentos")

def consultPagamentos():
    return controllerPagamentos.consultarPagamentos()


@app.post("/pagamentos")

def cadastrarPagamentos(
    tipo_pagamento: str = Body(embed = True),
    status_pagamento: str = Body(embed = True),
    valor_total: float = Body(embed = True),
):
    return controllerPagamentos.inserirPagamentos(tipo_pagamento, status_pagamento, valor_total)

@app.delete("/pagamentos")

def deletarPagamentos(id_pagamento: int = Body(embed = True)):
    controllerPagamentos.deletarPagamentos(id_pagamento)


@app.patch("/pagamentos")

def alterarPagamentos(tipo_pagamento: str = Body(embed = True) , status_pagamento: str = Body(embed = True), valor_total: int = Body(embed = True), idpagamentos: int = Body(embed = True)):
    return controllerPagamentos.alterarPagamentos(tipo_pagamento, status_pagamento, valor_total, idpagamentos)


##################################################################


@app.get("/itens_pedido")

def consultItensPedido():
    return controllerItensPedidos.consultarItensPedido()

@app.post("/itens_pedido")

def cadastrarItens_pedido(
    id_pedidos: int = Body(embed = True),
    nome_item: str = Body(embed = True),
    quantidade: int = Body(embed = True),
    preco_unitario: float = Body(embed = True)
):

    return controllerItensPedidos.inserirItensPedido(id_pedidos, nome_item, quantidade, preco_unitario)

@app.delete("/itens_pedido")

def apagarUsuarios(id_Item_Pedido: int = Body(embed = True)):
    return controllerItensPedidos.deletarItensPedido(id_Item_Pedido)


##########################################################


@app.get("/avaliacoes")

def consultavaliacoes():
    return controllerAvaliacoes.consultarAvaliacoes()

@app.post("/avaliacoes")

def cadastrarAvaliacoes(
    idPedido: int = Body(embed = True),
    notaServico: int = Body(embed = True),
    comentarioServico: str = Body(embed = True),
    
):
    return controllerAvaliacoes.inserirAvaliacoes(idPedido, notaServico, comentarioServico)

@app.delete("/avaliacoes")

def deletarAvaliacoes(id_avaliacao: int = Body(embed = True)):
    return controllerAvaliacoes.deletarAvaliacoes(id_avaliacao)
    

##########################################################


