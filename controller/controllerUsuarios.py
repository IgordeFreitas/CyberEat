import mysql.connector
from config.dbConfig import getConnection
from model.Usuarios.getUsuarios import queryUsuarios
from model.Usuarios.postUsuarios import insertUsuarios
from model.Usuarios.deleteUsuario import deleteUsuarios
from lib.Usuarios import Usuarios

############################################################################


def consultarUsuarios():
    connection = None
    try:
        connection = getConnection()
        query = queryUsuarios(connection)
        usuario = []        
        for row in query:
            user = Usuarios(row['nome'], row['email'], row['senha'], row['telefone'])
            usuario.append(user)
        return usuario
    finally:
        if connection:
            connection.close()

############################################################################

def inserirUsuario(nome, email, senha, telefone):
    connect = None 
    connect = getConnection()
    try:
        user = Usuarios(nome, email, senha, telefone)
        connect.start_transaction()
        linhasAfetadas = insertUsuarios(connect, user)
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
        print(error)
        connect.rollback()

    finally:
        if connect:
            connect.close()