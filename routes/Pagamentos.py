from fastapi import APIRouter, Body
from controller import controllerPagamentos
router = APIRouter()

@router.get("/pagamentos")

def consultPagamentos():
    return controllerPagamentos.consultarPagamentos()


@router.post("/pagamentos")

def cadastrarPagamentos(
    tipo_pagamento: str = Body(embed = True),
    status_pagamento: str = Body(embed = True),
    valor_total: float = Body(embed = True),
):
    return controllerPagamentos.inserirPagamentos(tipo_pagamento, status_pagamento, valor_total)

@router.delete("/pagamentos")

def deletarPagamentos(id_pagamento: int = Body(embed = True)):
    controllerPagamentos.deletarPagamentos(id_pagamento)


@router.patch("/pagamentos")

def alterarPagamentos(tipo_pagamento: str = Body(embed = True) , status_pagamento: str = Body(embed = True), valor_total: str = Body(embed = True), idpagamento: int = Body(embed = True)):
    return     controllerPagamentos.alterarPagamentos(tipo_pagamento, status_pagamento,  valor_total, idpagamento)
