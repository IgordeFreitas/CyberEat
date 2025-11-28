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
            user = Produtos(row['id_restaurantes'], row['descricao'])
            produtos.append(user)
        return produtos
    finally:
        if connection:
            connection.close()

############################################################################

def inserirProdutos(id_restaurantes, descricao):
    connect = None 
    connect = getConnection()
    try:
        user = Produtos(id_restaurantes, descricao)
        connect.start_transaction()
        linhasAfetadas = insertProdutos(connect, user)
        connect.commit()
        if linhasAfetadas == 1:
            return "Usuario cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
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