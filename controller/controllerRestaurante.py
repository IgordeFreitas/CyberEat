import mysql.connector
from config.dbConfig import getConnection
from model.Restaurantes.getRestaurantes import queryRestaurantes
from model.Restaurantes.postRestaurantes import insertRestaurantes
from model.Restaurantes.deleteRestaurantes import deleteRestaurantes
from lib.Restaurante import Restaurante

############################################################################


def consultarRestaurantes():
    connection = None
    try:
        connection = getConnection()
        query = queryRestaurantes(connection)
        restaurante = []        
        for row in query:
            user = Restaurante(row['id_Produto'], row['id_Usuarios'], row['id_Endenreco'], row['nome'], row['categoria'])
            restaurante.append(user)
        return restaurante
    finally:
        if connection:
            connection.close()

############################################################################

def inserirRestaurantes(id_Produto, id_Usuarios, id_Endenreco, nome, categoria):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertRestaurantes(connect, id_Produto, id_Usuarios, id_Endenreco, nome, categoria)
        connect.commit()
        if linhasAfetadas == 1:
            return "Restaurante cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarRestaurante(id_Restaurantes):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deleteRestaurantes(connect, id_Restaurantes)
        connect.commit()
        if linhasAfetadas == 1:
            return "Restaurante excluido com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()