import mysql.connector
from config.dbConfig import getConnection
from model.Avaliacoes.getAvaliacoes import queryAvaliacoes
from model.Avaliacoes.postAvaliacoes import insertAvaliacoes
from model.Avaliacoes.deleteAvaliacoes import deleteAvaliacoes
from model.Avaliacoes.updateAvaliacoes import updateAvaliacoes
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


def inserirAvaliacoes(idPedido, notaServico, comentarioServico):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertAvaliacoes(connect, idPedido, notaServico, comentarioServico)
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
        print(f'Erro {error}')
        connect.rollback()

    finally:
        if connect:
            connect.close()

def alterarAvaliacoes( id_pedidos, nota, comentario, id_avaliacao):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = updateAvaliacoes(connect, id_pedidos, nota, comentario, id_avaliacao )
        connect.commit()
        if linhasAfetadas == 1:
            return "Avaliaçao alterado com sucesso"
    except mysql.connector.Error as error:
        connect.rollback()
        return f'ERRO - {error}'

    finally:
        if connect:
            connect.close()