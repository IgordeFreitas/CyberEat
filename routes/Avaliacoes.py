from fastapi import APIRouter, Body
from controller import controllerAvaliacoes
router = APIRouter()



@router.get("/avaliacoes")

def consultavaliacoes():
    return controllerAvaliacoes.consultarAvaliacoes()

@router.post("/avaliacoes")

def cadastrarAvaliacoes(
    idPedido: int = Body(embed = True),
    notaServico: int = Body(embed = True),
    comentarioServico: str = Body(embed = True),
    
):
    return controllerAvaliacoes.inserirAvaliacoes(idPedido, notaServico, comentarioServico)

@router.delete("/avaliacoes")

def deletarAvaliacoes(id_avaliacao: int = Body(embed = True)):
    return controllerAvaliacoes.deletarAvaliacoes(id_avaliacao)

@router.patch("/avaliacoes")

def alterarAvaliacoes(
    id_pedidos: int = Body(embed = True),
    nota: int = Body(embed = True),
    comentario: str = Body(embed = True),
    id_avaliacao: int = Body(embed = True)
):
    return controllerAvaliacoes.alterarAvaliacoes(id_pedidos, nota, comentario, id_avaliacao)

