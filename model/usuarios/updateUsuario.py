def updateUsuario(connctionDB, nome, email, senha, telefone, idUsuario):
    cursor = connctionDB.cursor(dictionary = True)
    cursor.execute('UPDATE usuarios SET nome = %s, email = %s, nome_restaurante = %s, telefone = %s WHERE id_usuarios = %s',
                   (nome, email, senha, telefone, idUsuario))    

    cursor.fetchall()
    cursor.close()
    return cursor.rowcount