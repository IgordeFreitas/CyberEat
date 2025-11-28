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
    id_pagamento: int = Body(embed = True),
    id_Entrega: int = Body(embed = True),
):
    return controllerPedidos.inserirPedidos(id_restaurantes, id_usuarios, id_Endereco, id_pagamento, id_Entrega)

@app.delete("/pedidos")

def deletarPedidos(id_pedido: int = Body(embed = True)):
    controllerPedidos.deletarPedidos(id_pedido)


#################################################################  Abaixo, tudo sobre a rota /entregas

@app.get("/entregas")

def consultEntregas():
    return controllerEntregas.consultarEntregas()

@app.post("/entregas")

def cadastrarEntrega(
    id_endereco: int = Body(embed = True),
    data_entrega: int = Body(embed = True)
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
    descricao: int = Body(embed = True)
):
   
    return controllerProdutos.inserirProdutos(id_restaurantes, descricao)

@app.delete("/produtos")

def apagarProdutos(id_produto: int = Body(embed = True)):
    return controllerProdutos.deletarProdutos(id_produto)


########################################################

@app.get("/pagamentos")

def consultPagamentos():
    return controllerPagamentos.consultarPagamentos()


@app.post("/pagamentos")

def cadastrarPagamentos(
    tipo_pagamento: int = Body(embed = True),
    status_pagamento: int = Body(embed = True),
    valor_total: int = Body(embed = True),
    
):
    return controllerPagamentos.inserirPagamentos(tipo_pagamento, status_pagamento, valor_total)

@app.delete("/pagamentos")

def deletarPagamentos(id_pagamento: int = Body(embed = True)):
    controllerPagamentos.deletarPagamentos(id_pagamento)


#############################################


@app.get("/itens_pedido")

def consultItensPedido():
    return controllerItensPedidos.consultarItensPedido()

@app.post("/itens_pedido")

def cadastrarItens_pedido(
    id_pedidos: str = Body(embed = True),
    nome_item: str = Body(embed = True),
    quantidade: str = Body(embed = True),
    preco_unitario: str = Body(embed = True)
):

    return controllerItensPedidos.inserirItens_pedido(id_pedidos, nome_item, quantidade, preco_unitario)

@app.delete("/itens_pedido")

def apagarUsuarios(id_Item_Pedido: int = Body(embed = True)):
    return controllerItensPedidos.deletarItensPedido(id_Item_Pedido)


##########################################################


@app.get("/avaliacoes")

def consultavaliacoes():
    return controllerAvaliacoes.consultarAvaliacoes()

@app.post("/avaliacoes")

def cadastrarAvaliacoes(
    notaServico: int = Body(embed = True),
    comentarioServico: int = Body(embed = True),
    
):
    return controllerAvaliacoes.inserirAvaliacoess(notaServico, comentarioServico)

@app.delete("/avaliacoes")

def deletarAvaliacoes(id_avaliacao: int = Body(embed = True)):
    return controllerAvaliacoes.deletarAvaliacoes(id_avaliacao)
    

