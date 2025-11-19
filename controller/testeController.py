from config.dbConfig import getConnection
from model.testeModel import queryUsuarios, queryRestaurantes
def consultarUsuarios():
    connection = None
    try:
        connection = getConnection()
        
        return queryUsuarios(connection)
    finally:
        if connection:
            connection.close()

def consultarRestaurantes():
    conect = None
    try:
        conect = getConnection()
        return queryRestaurantes(conect)
    except:
        print('Erro')