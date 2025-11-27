import mysql.connector
from config.dbConfig import getConnection
from model.Enderecos.getEndereco import queryEndereco
from model.Enderecos.postEnderecos import insertEnderecos
from model.Enderecos.deleteEnderecos import deleteEnderecos
from lib.Endereco import Endereco




def consultarEndereco():
    connection = None
    try:
        connection = getConnection()
        query = queryEndereco(connection)
        endereco = []        
        for row in query:
            user = Endereco(row['id_usuario'], row['bairro'])
            endereco.append(user)
        return endereco
    finally:
        if connection:
            connection.close()


def inserirEndereco(id_usuario, bairro):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertEnderecos(connect, id_usuario, bairro)
        connect.commit()
        if linhasAfetadas == 1:
            return "Endereco cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarEndereco(id_Enderecos):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deleteEnderecos(connect, id_Enderecos)
        connect.commit()
        if linhasAfetadas == 1:
            return "Endereco excluido com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()