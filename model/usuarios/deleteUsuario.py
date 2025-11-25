def deleteUsuarios(conectionDB, idUsuario):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM usuarios WHERE id_usuarios = %s', (idUsuario))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount