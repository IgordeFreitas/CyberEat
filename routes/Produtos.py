from fastapi import APIRouter, Body
from controller import controllerProdutos
router = APIRouter()


@router.get("/produtos")

def consultProdutos():
    return controllerProdutos.consultarProdutos()

@router.post("/produtos")

def cadastrarProdutos(
    id_restaurantes: int = Body(embed = True),
    descricao: str = Body(embed = True)
):
   
    return controllerProdutos.inserirProdutos(id_restaurantes, descricao)

@router.delete("/produtos")

def apagarProdutos(id_produto: int = Body(embed = True)):
    return controllerProdutos.deletarProdutos(id_produto)


@router.patch("/produtos")

def alterarProdutos(
    idRestaurante: int = Body(embed = True),
    descricao: str = Body(embed = True),
    idProduto: int = Body(embed = True)
):
    return controllerProdutos.alterarProdutos(idRestaurante, descricao, idProduto)

