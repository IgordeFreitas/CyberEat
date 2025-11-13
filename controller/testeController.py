from config.dbConfig import getConnection

def consultarUsuarios():
    connection = None
    try:
        connection = getConnection()
        cursor = connection.cursor(dictionary = True)
        cursor.execute('SELECT nome, email, senha, telefone FROM usuarios')
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios
    finally:
        if connection:
            connection.close()