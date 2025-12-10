from model.Login.Login import loginUsuario
from config.dbConfig import getConnection


def verificarUsuario(nome, senha):
    connection = None
    connection = getConnection()
    return loginUsuario(connection, nome, senha)
    