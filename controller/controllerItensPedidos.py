import mysql.connector
from config.dbConfig import getConnection
from model.ItensPedido.getItensPedido import queryItensPedido
from model.ItensPedido.postItensPedido import insertItensPedido
from model.ItensPedido.deleteItensPedido import deleteItensPedido
from model.ItensPedido.updateItensPedido import updateItensPedido
from lib.ItensPedido import ItensPedido

############################################################################


def consultarItensPedido():
    connection = None
    try:
        connection = getConnection()
        query = queryItensPedido(connection)
        itensPedido = []        
        for row in query:
            user = ItensPedido(row['id_pedidos'], row['nome_item'], row['quantidade'], row['preco_unitario'])
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
        linhasAfetadas = insertItensPedido(connect, id_Pedido, nomeItem, quantidadeItem, precoUnitario)
        connect.commit()
        if linhasAfetadas == 1:
            return "Itens do pedido cadastrado com sucesso"
    except mysql.connector.Error as error:
        print(f'Erro {error}')
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
        print(f'Erro {error}')
        connect.rollback()

    finally:
        if connect:
            connect.close()



def alterarItensPedido(id_pedidos, nome_item, quantidade, preco_unitario, id_item_pedido):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = updateItensPedido(connect, id_pedidos, nome_item, quantidade, preco_unitario, id_item_pedido)
        connect.commit()
        if linhasAfetadas == 1:
            return "Item pedido alterado com sucesso"
    except mysql.connector.Error as error:
        connect.rollback()
        return f'ERRO - {error}'

    finally:
        if connect:
            connect.close()