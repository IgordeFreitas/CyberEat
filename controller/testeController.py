from config.dbConfig import getConnection
from model.testeModel import queryUsuarios
def consultarUsuarios():
    connection = None
    try:
        connection = getConnection()
        
        return queryUsuarios(connection)
    finally:
        if connection:
            connection.close()
