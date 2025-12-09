from fastapi import APIRouter, Body
from controller import controllerPedidos
router = APIRouter()


@router.get("/pedidos")

def consultPedidos():
    return controllerPedidos.consultarPedidos()


@router.post("/pedidos")

def cadastrarPedidos(
    id_restaurantes: int = Body(embed = True),
    id_usuarios: int = Body(embed = True),
    id_Endereco: int = Body(embed = True),
    id_pagamento: int = Body(embed = True),
    id_Entrega: int = Body(embed = True),
):
    return controllerPedidos.inserirPedidos(id_restaurantes, id_usuarios, id_Endereco, id_pagamento, id_Entrega)

@router.delete("/pedidos")

def deletarPedidos(id_pedido: int = Body(embed = True)):
    controllerPedidos.deletarPedidos(id_pedido)


@router.patch('/pedidos')

def alterarPedido(
    id_restaurante: int = Body(embed = True), 
    id_usuarios: int = Body(embed = True), 
    id_endereco: int = Body(embed = True), 
    id_pagamento: int = Body(embed = True), 
    id_entrega: int = Body(embed = True), 
    idPedido: int = Body(embed = True)
):
    return controllerPedidos.alterarPedidos(id_restaurante, id_usuarios, id_endereco, id_pagamento, id_entrega, idPedido)
