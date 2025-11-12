from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/produtos")

def cadastrarProduto(nome: str = Body(embed = True), preco: float = Body(embed = True)):
    return {
        'ação': 'Cadastrar produto', 
        'nome': nome,
        'preco': preco
    }

@app.get("/")

def returnal():
    return{
        'Mensagem': 'Hello World'
    }