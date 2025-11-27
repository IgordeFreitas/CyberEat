import mysql.connector
from config.dbConfig import getConnection
from model.Entregas.getEntregas import queryEntregas
from model.Entregas.postEntregas import insertEntregas
from model.Entregas.deleteEntregas import deleteEntregas
from lib.Entregas import Entregas

############################################################################


def consultarEntregas():
    connection = None
    try:
        connection = getConnection()
        query = queryEntregas(connection)
        entrega = []        
        for row in query:
            user = Entregas(row['idIndereco'], row['dataEntrega'])
            entrega.append(user)
        return entrega
    finally:
        if connection:
            connection.close()

############################################################################

def inserirEntregas(id_Indereco, dataEntrega):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertEntregas(connect, id_Indereco, dataEntrega)
        connect.commit()
        if linhasAfetadas == 1:
            return "Entrega cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarEntregas(id_Entregas):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deleteEntregas(connect, id_Entregas)
        connect.commit()
        if linhasAfetadas == 1:
            return "Entrega excluido com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()