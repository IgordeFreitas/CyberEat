import mysql.connector
from config.dbConfig import getConnection
from model.ItensPedido.getItensPedido import queryItensPedido
from model.ItensPedido.postItensPedido import insertItensPedido
from model.ItensPedido.deleteItensPedido import deleteItensPedido
from lib.ItensPedido import ItensPedido

############################################################################


def consultarItensPedido():
    connection = None
    try:
        connection = getConnection()
        query = queryItensPedido(connection)
        itensPedido = []        
        for row in query:
            user = ItensPedido(row['id_pedidos'], row['nome_item'], row['quantidade_item'], row['preco_unitario'])
            itensPedido.append(user)
        return itensPedido
    finally:
        if connection:
            connection.close()

############################################################################

def inserirItensPedido(id_Pedido, nomeItem, quantidadeItem, precoUnitario):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertItensPedido(id_Pedido, nomeItem, quantidadeItem, precoUnitario)
        connect.commit()
        if linhasAfetadas == 1:
            return "ItensPedido cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarItensPedido(id_ItensPedido):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deleteItensPedido(connect, id_ItensPedido)
        connect.commit()
        if linhasAfetadas == 1:
            return "ItensPedido excluido com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()