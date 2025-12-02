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
            user = Restaurante(row['id_usuarios'], row['id_endereco'], row['nome_restaurante'], row['categoria'])
            restaurante.append(user)
        return restaurante
    finally:
        if connection:
            connection.close()

############################################################################

def inserirRestaurantes(id_Usuarios, id_Endenreco, nome_restaurante, categoria):
    connect = None 
    connect = getConnection()
    try:
        restaurante = Restaurante(id_Usuarios, id_Endenreco, nome_restaurante, categoria)
        connect.start_transaction()
        linhasAfetadas = insertRestaurantes(connect, restaurante)
        connect.commit()
        if linhasAfetadas == 1:
            return "Restaurante cadastrado com sucesso"
    except mysql.connector.Error as error:
        print(f'Erro {error}')
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
        print(error)
        connect.rollback()

    finally:
        if connect:
            connect.close()