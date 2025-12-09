from fastapi import APIRouter, Body
from controller import controllerItensPedidos
router = APIRouter()


@router.get("/itens_pedido")

def consultItensPedido():
    return controllerItensPedidos.consultarItensPedido()

@router.post("/itens_pedido")

def cadastrarItens_pedido(
    id_pedidos: int = Body(embed = True),
    nome_item: str = Body(embed = True),
    quantidade: int = Body(embed = True),
    preco_unitario: float = Body(embed = True)
):

    return controllerItensPedidos.inserirItensPedido(id_pedidos, nome_item, quantidade, preco_unitario)

@router.delete("/itens_pedido")

def apagarItensPedido(id_Item_Pedido: int = Body(embed = True)):
    return controllerItensPedidos.deletarItensPedido(id_Item_Pedido)


@router.patch("/itens_pedido")

def alterarItens_pedido(
    id_pedidos: int = Body(embed = True),
    nome_item: str = Body(embed = True),
    quantidade: int = Body(embed = True),
    preco_unitario: float = Body(embed = True),
    id_item_pedido: int = Body(embed = True)
):
    return controllerItensPedidos.alterarItensPedido(id_pedidos, nome_item, quantidade, preco_unitario, id_item_pedido)
