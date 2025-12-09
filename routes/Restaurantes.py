from fastapi import APIRouter, Body
from controller import controllerRestaurante 
router = APIRouter()



@router.get("/restaurantes")

def restaurantes():
    return controllerRestaurante.consultarRestaurantes()

@router.post("/restaurantes")

def cadastrarRestaurante(
    id_usuario: int = Body(embed = True),
    id_endereco: int = Body(embed = True),
    nome_restaurante: str = Body(embed = True),
    categoria: str = Body(embed = True),
):
    return controllerRestaurante.inserirRestaurantes(id_usuario, id_endereco, nome_restaurante, categoria)

@router.delete("/restaurantes")

def deletarRestaurantes(id_restaurantes: int = Body(embed = True)):
    return controllerRestaurante.deletarRestaurante(id_restaurantes)

@router.patch("/restaurantes")

def alterarRestaurante(
       idUsuario: int = Body(embed = True),
       idEndereco: int = Body(embed = True),
       nomeRestaurante: str = Body(embed = True),
       categoria: str = Body(embed = True),
       idRestaurante: int = Body(embed = True)
):
    return controllerRestaurante.alterarRestaurante(idUsuario, idEndereco, nomeRestaurante, categoria, idRestaurante)
    