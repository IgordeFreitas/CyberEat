def deleteItensPedido(conectionDB, idItensPedido):
    cursor = conectionDB.cursor(dictionary = True)
    cursor.execute('DELETE FROM itensPedido WHERE id_ItensPedido = %s', (idItensPedido))
    cursor.fetchall()
    cursor.close()
    return cursor.rowcount
