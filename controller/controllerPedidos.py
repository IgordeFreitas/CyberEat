import mysql.connector
from config.dbConfig import getConnection
from model.Pedidos.getPedidos import queryPedidos
from model.Pedidos.postPedidos import insertPedidos
from model.Pedidos.deletePedidos import deletePedidos
from model.Pedidos.updatePedidos import updatePedidos
from lib.Pedidos import Pedidos

############################################################################


def consultarPedidos():
    connection = None
    try:
        connection = getConnection()
        query = queryPedidos(connection)
        pedido = []        
        for row in query:
            user = Pedidos(row['id_restaurantes'], row['id_usuarios'], row['id_endereco'], row['id_pagamento'], row['id_entrega'])
            pedido.append(user)
        return pedido
    finally:
        if connection:
            connection.close()

############################################################################

def inserirPedidos(id_Restaurantes, id_Usuarios, id_Endereco, id_Pagamento, id_Entrega):
    connect = None 
    connect = getConnection()
    try:
        pedido = Pedidos(id_Restaurantes, id_Usuarios, id_Endereco, id_Pagamento, id_Entrega)
        connect.start_transaction()
        linhasAfetadas = insertPedidos(connect, pedido)
        connect.commit()
        if linhasAfetadas == 1:
            return "Pedido cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarPedidos(id_Produtos):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deletePedidos(connect, id_Produtos)
        connect.commit()
        if linhasAfetadas == 1:
            return "Produto excluido com sucesso"
    except mysql.connector.Error as error:
        print(f'ERRO - {error}')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################


def alterarPedidos(id_restaurante, id_usuarios, id_endereco, id_pagamento, id_entrega, idPedido):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = updatePedidos(connect, id_restaurante, id_usuarios, id_endereco, id_pagamento, id_entrega, idPedido)
        connect.commit()
        if linhasAfetadas == 1:
            return "Pedido alterado com sucesso"
    except mysql.connector.Error as error:
        connect.rollback()
        return f'ERRO - {error}'

    finally:
        if connect:
            connect.close()