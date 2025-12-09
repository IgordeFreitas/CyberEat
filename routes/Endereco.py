from fastapi import APIRouter, Body
from controller import controllerEndereco
router = APIRouter()


@router.get("/endereco")

def consultEndereco():
    return controllerEndereco.consultarEndereco()

@router.post("/endereco")

def cadastrarEndereco(
    id_usuarios: int = Body(embed = True),
    bairro: int = Body(embed = True),    
):
    return controllerEndereco.inserirEndereco(id_usuarios, bairro)

@router.delete("/endereco")

def deletarEndereco(id_endereco: int = Body(embed = True)):
    return controllerEndereco.deletarEndereco(id_endereco)

@router.patch("/endereco")

def alterarEndereco(
    id_usuarios: int = Body(embed = True),
    bairro: str = Body(embed = True),
    id_endereco: int = Body(embed = True)
):
    return controllerEndereco.alterarEndereco(id_usuarios, bairro, id_endereco)
