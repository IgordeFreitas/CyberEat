import mysql.connector
from config.dbConfig import getConnection
from model.usuarios.getUsuarios import queryUsuarios
from model.usuarios.postUsuarios import insertUsuarios
from model.usuarios.deleteUsuario import deleteUsuarios

from lib import * 


def consultarUsuarios():
    connection = None
    try:
        connection = getConnection()
        return queryUsuarios(connection) 
    finally:
        if connection:
            connection.close()

############################################################################

def inserirUsuario(nome, email, senha, telefone):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = insertUsuarios(connect, nome, email, senha, telefone)
        connect.commit()
        if linhasAfetadas == 1:
            return "Usuario cadastrado com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()

############################################################################

def deletarUsuario(idUsuarios):
    connect = None 
    connect = getConnection()
    try:
        connect.start_transaction()
        linhasAfetadas = deleteUsuarios(connect, idUsuarios)
        connect.commit()
        if linhasAfetadas == 1:
            return "Usuario excluido com sucesso"
    except mysql.connector.Error as error:
        print('Erro')
        connect.rollback()

    finally:
        if connect:
            connect.close()