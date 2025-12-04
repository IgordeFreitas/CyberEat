import mysql.connector
from config.dbConfig import getConnection
from model.Pagamentos.getPagamentos import queryPagamentos
from model.Pagamentos.postPagamentos import insertPagamentos
from model.Pagamentos.deletePagamentos import deletePagamentos
from model.Pagamentos.updatePagamentos import updatePagamentos
from lib.Pagamentos import Pagamentos

############################################################################


def consultarPagamentos():
    connection = None
    try:
        connection = getConnection()
        query = queryPagamentos(connection)
        pagamento = []        
        for row in query:
            user = Pagamentos(row['tipo_pagamento'], row['status_pagamento'], row['valor_total'])
            pagamento.append(user)
        return pagamento
    finally:
        if connection:
            connection.close()

############################################################################

def inserirPagamentos(tipoPagamento, statusPagamento, valorTotal):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertPagamentos(connect, tipoPagamento, statusPagamento, valorTotal)
        connect.commit()
        if linhasAfetadas == 1:
            return "Pagamento cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarPagamentos(id_Pagamentos):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deletePagamentos(connect, id_Pagamentos)
        connect.commit()
        if linhasAfetadas == 1:
            return "Pagamento excluido com sucesso"
    except mysql.connector.Error as error:
        print(f'Erro {error}')
        connect.rollback()

    finally:
        if connect:
            connect.close()


def alterarPagamentos(tipo_pagamento, status_pagamento, valor_total, idpagamento):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = updatePagamentos(connect, tipo_pagamento, status_pagamento, valor_total, idpagamento)
        connect.commit()
        if linhasAfetadas == 1:
            return "Pagamento alterado com sucesso"
    except mysql.connector.Error as error:
        connect.rollback()
        return f'ERRO - {error}'

    finally:
        if connect:
            connect.close()