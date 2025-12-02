import mysql.connector
from config.dbConfig import getConnection
from model.Produtos.getProdutos import queryProdutos
from model.Produtos.postProdutos import insertProdutos
from model.Produtos.deleteProdutos import deleteProdutos
from lib.Produtos import Produtos

############################################################################


def consultarProdutos():
    connection = None
    try:
        connection = getConnection()
        query = queryProdutos(connection)
        produtos = []        
        for row in query:
            product = Produtos(row['id_restaurante'], row['descricao'])
            produtos.append(product)
        return produtos
    finally:
        if connection:
            connection.close()

############################################################################

def inserirProdutos(id_restaurantes, descricao):
    connect = None 
    connect = getConnection()
    try:
        produto = Produtos(id_restaurantes, descricao)
        connect.start_transaction()
        linhasAfetadas = insertProdutos(connect, produto)
        connect.commit()
        if linhasAfetadas == 1:
            return "Produto cadastrado com sucesso"
    except mysql.connector.Error as error:
        print(f'Erro {error}')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarProdutos(id_Produtos):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deleteProdutos(connect, id_Produtos)
        connect.commit()
        if linhasAfetadas == 1:
            return "Produto excluido com sucesso"

    except mysql.connector.Error as error:
        print(error)
        connect.rollback()

    finally:
        if connect:
            connect.close()