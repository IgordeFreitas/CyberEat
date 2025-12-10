from fastapi import APIRouter, Body
from controller.controllerLogin import verificarUsuario

router = APIRouter()


@router.post("/login")

def login(usuario: str = Body(embed = True), 
          senha: str = Body(embed = True)):
    return verificarUsuario(usuario, senha)