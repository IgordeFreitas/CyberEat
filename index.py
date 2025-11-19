from fastapi import FastAPI, Body
from controller.testeController import consultarUsuarios, consultarRestaurantes

app = FastAPI()

@app.post("/produtos")

def cadastrarProduto(nome: str = Body(embed = True), preco: float = Body(embed = True)):
    return {
        'ação': 'Cadastrar produto', 
        'nome': nome,
        'preco': preco
    }

@app.get("/")

def inicio():
    return consultarUsuarios()

@app.get("/restaurante")

def restaurantes():
    return consultarRestaurantes()

@app.post("/clientes")
    
def cadastrarClientes(nome: str = Body(embed = True), email: str = Body(embed = True), senha: str = Body(embed = True), telefone: str = Body(embed = True)):
    return {
        'ação': 'Cadastrar Cliente',
        'nome': nome,
        'emial': email,
        'senha': senha,
        'telefone': telefone
    }

@app.post("/restaurante")

def cadastrarRestaurante(nome: str = Body(embed = True), telefone: str = Body(embed = True), descricao: str = Body(embed = True), endereco: str = Body(embed = True), aberto: bool = Body(embed = True), taxaEntrega: float = Body(embed = True), tempoMedioMinutos: int = Body(embed = True), criadoEm: int = Body(embed = True)):
    return {
        'nome' : nome,
        'telefone' : telefone,
        'descricao' : descricao,
        'endereco': endereco,
        'aberto': aberto,
        'taxa_entrega': taxaEntrega,
        'tempo_medio_em_minutos' : tempoMedioMinutos,
        'ano_criação' : criadoEm
    }