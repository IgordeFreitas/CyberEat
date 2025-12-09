from fastapi import APIRouter, Body
from controller import controllerUsuarios
router = APIRouter()


@router.get("/usuarios")

def consultUsuarios():
    return controllerUsuarios.consultarUsuarios()

@router.post("/usuarios")

def cadastrarUsuario(
    nome: str = Body(embed = True),
    email: str = Body(embed = True),
    senha: str = Body(embed = True),
    telefone: str = Body(embed = True)
):
   
    return controllerUsuarios.inserirUsuario(nome, email, senha, telefone)

@router.delete("/usuarios")

def apagarUsuarios(idUsuario: int = Body(embed = True)):
    return controllerUsuarios.deletarUsuario(idUsuario)

@router.patch("/usuarios")

def alterarUsuario(
    nome: str = Body(embed = True),
    email: str = Body(embed = True),
    senha: str = Body(embed = True),
    telefone: str = Body(embed = True),
    idUsuario: int = Body(embed = True)
):
    return controllerUsuarios.atualizarUsuario(nome, email, senha, telefone, idUsuario)