from ..config.dbConfig import getConnection

class TesteController():
    def consultarUsuarios():
        try:
            connection = getConnection()

        finally:
            if connection:
                connection.close()