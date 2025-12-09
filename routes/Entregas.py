from fastapi import APIRouter, Body
from controller import controllerEntregas
router = APIRouter()


@router.get("/entregas")

def consultEntregas():
    return controllerEntregas.consultarEntregas()

@router.post("/entregas")

def cadastrarEntrega(
    id_endereco: int = Body(embed = True),
    data_entrega: str = Body(embed = True)
):
   
    return controllerEntregas.inserirEntregas(id_endereco, data_entrega)

@router.delete("/entregas")

def apagarUsuarios(id_entrega: int = Body(embed = True)):
    return controllerEntregas.deletarEntregas(id_entrega)


@router.patch("/entregas")
def alterarEntregas(
    id_endereco: int = Body(embed = True),
    data_entrega: str = Body(embed = True),
    id_entrega: int = Body(embed = True),

):
    return controllerEntregas.alterarEntregas(id_endereco, data_entrega, id_entrega)
