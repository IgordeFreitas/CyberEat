import mysql.connector
from config.dbConfig import getConnection
from model.Avaliacoes.getAvaliacoes import queryAvaliacoes
from model.Avaliacoes.postAvaliacoes import insertAvaliacoes
from model.Avaliacoes.deleteAvaliacoes import deleteAvaliacoes
from lib.Avaliacoes import Avaliacoes




def consultarAvaliacoes():
    connection = None
    try:
        connection = getConnection()
        query = queryAvaliacoes(connection)
        avaliacoes = []        
        for row in query:
            user = Avaliacoes(row['id_pedidos'] ,row['nota'], row['comentario'])
            avaliacoes.append(user)
        return avaliacoes
    finally:
        if connection:
            connection.close()


def inserirAvaliacoes(id_Avaliacoes, notaServico, comentarioServico):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertAvaliacoes(connect, id_Avaliacoes, notaServico, comentarioServico)
        connect.commit()
        if linhasAfetadas == 1:
            return "Avaliacoes cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarAvaliacoes(id_Avaliacoes):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deleteAvaliacoes(connect, id_Avaliacoes)
        connect.commit()
        if linhasAfetadas == 1:
            return "Avaliacoes excluido com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()