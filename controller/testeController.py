from config.dbConfig import getConnection

class TesteController():
    def consultarUsuarios():
        connection = None

        try:
            connection = getConnection()

            cursor = connection.cursor(
                dictionary = True)

        finally:
            if connection:
                connection.close()

