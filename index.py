from fastapi import FastAPI
from routes import (Avaliacoes, Usuarios, Endereco, Entregas, Pagamentos, Produtos, Pedidos, itensPedidos)

app = FastAPI()

app.include_router(Avaliacoes.router)
app.include_router(Usuarios.router)
app.include_router(Endereco.router)
app.include_router(Entregas.router)
app.include_router(Pagamentos.router)
app.include_router(Produtos.router)
app.include_router(Pedidos.router)
app.include_router(itensPedidos.router)
